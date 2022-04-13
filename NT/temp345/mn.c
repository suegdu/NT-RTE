#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "SigProc_FIX.h"
#include "tables.h"

#define BIN_DIV_STEPS_A2NLSF_FIX      3 
#define MAX_ITERATIONS_A2NLSF_FIX    16


static OPUS_INLINE void silk_A2NLSF_trans_poly(
    opus_int32          *p,                    
    const opus_int      dd                      
)
{
    opus_int k, n;

    for( k = 2; k <= dd; k++ ) {
        for( n = dd; n > k; n-- ) {
            p[ n - 2 ] -= p[ n ];
        }
        p[ k - 2 ] -= silk_LSHIFT( p[ k ], 1 );
    }
}

static OPUS_INLINE opus_int32 silk_A2NLSF_eval_poly( 
    opus_int32          *p,                    
    const opus_int32    x,                     
    const opus_int      dd                     
)
{
    opus_int   n;
    opus_int32 x_Q16, y32;

    y32 = p[ dd ];                                  /* Q16 */
    x_Q16 = silk_LSHIFT( x, 4 );

    if ( opus_likely( 8 == dd ) )
    {
        y32 = silk_SMLAWW( p[ 7 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 6 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 5 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 4 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 3 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 2 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 1 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 0 ], y32, x_Q16 );
    }
    else
    {
        for( n = dd - 1; n >= 0; n-- ) {
            y32 = silk_SMLAWW( p[ n ], y32, x_Q16 );    /* Q16 */
        }
    }
    return y32;
}

static OPUS_INLINE void silk_A2NLSF_init(
     const opus_int32    *a_Q16,
     opus_int32          *P,
     opus_int32          *Q,
     const opus_int      dd
)
{
    opus_int k;

   
    P[dd] = silk_LSHIFT( 1, 16 );
    Q[dd] = silk_LSHIFT( 1, 16 );
    for( k = 0; k < dd; k++ ) {
        P[ k ] = -a_Q16[ dd - k - 1 ] - a_Q16[ dd + k ];    /* Q16 */
        Q[ k ] = -a_Q16[ dd - k - 1 ] + a_Q16[ dd + k ];    /* Q16 */
    }


    for( k = dd; k > 0; k-- ) {
        P[ k - 1 ] -= P[ k ];
        Q[ k - 1 ] += Q[ k ];
    }

    
    silk_A2NLSF_trans_poly( P, dd );
    silk_A2NLSF_trans_poly( Q, dd );
}


void silk_A2NLSF(
    opus_int16                  *NLSF,              
    opus_int32                  *a_Q16,            
    const opus_int              d                   
)
{
    opus_int   i, k, m, dd, root_ix, ffrac;
    opus_int32 xlo, xhi, xmid;
    opus_int32 ylo, yhi, ymid, thr;
    opus_int32 nom, den;
    opus_int32 P[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 Q[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 *PQ[ 2 ];
    opus_int32 *p;

    
    PQ[ 0 ] = P;
    PQ[ 1 ] = Q;

    dd = silk_RSHIFT( d, 1 );

    silk_A2NLSF_init( a_Q16, P, Q, dd );

    
    p = P;                          

    xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );

    if( ylo < 0 ) {
        */
        NLSF[ 0 ] = 0;
        p = Q;                      
        ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
        root_ix = 1;                
    } else {
        root_ix = 0;            
    }
    k = 1;                          
    i = 0;                         
    thr = 0;
    while( 1 ) {
        
        xhi = silk_LSFCosTab_FIX_Q12[ k ]; /* Q12 */
        yhi = silk_A2NLSF_eval_poly( p, xhi, dd );

        
        if( ( ylo <= 0 && yhi >= thr ) || ( ylo >= 0 && yhi <= -thr ) ) {
            if( yhi == 0 ) {
              
              
                thr = 1;
            } else {
                thr = 0;
            }
           
            ffrac = -256;
            for( m = 0; m < BIN_DIV_STEPS_A2NLSF_FIX; m++ ) {
                /* Evaluate polynomial */
                xmid = silk_RSHIFT_ROUND( xlo + xhi, 1 );
                ymid = silk_A2NLSF_eval_poly( p, xmid, dd );

                
                if( ( ylo <= 0 && ymid >= 0 ) || ( ylo >= 0 && ymid <= 0 ) ) {
                    
                    xhi = xmid;
                    yhi = ymid;
                } else {
                    
                    xlo = xmid;
                    ylo = ymid;
                    ffrac = silk_ADD_RSHIFT( ffrac, 128, m );
                }
            }

            
            if( silk_abs( ylo ) < 65536 ) {
               
                den = ylo - yhi;
                nom = silk_LSHIFT( ylo, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) + silk_RSHIFT( den, 1 );
                if( den != 0 ) {
                    ffrac += silk_DIV32( nom, den );
                }
            } else {
                
                ffrac += silk_DIV32( ylo, silk_RSHIFT( ylo - yhi, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) );
            }
            NLSF[ root_ix ] = (opus_int16)silk_min_32( silk_LSHIFT( (opus_int32)k, 8 ) + ffrac, silk_int16_MAX );

            silk_assert( NLSF[ root_ix ] >= 0 );

            root_ix++;        
            if( root_ix >= d ) {
               
                break;
            }
            /* Alternate pointer to polynomial */
            p = PQ[ root_ix & 1 ];

            /
            xlo = silk_LSFCosTab_FIX_Q12[ k - 1 ]; /* Q12*/
            ylo = silk_LSHIFT( 1 - ( root_ix & 2 ), 12 );
        } else {
            
            k++;
            xlo = xhi;
            ylo = yhi;
            thr = 0;

            if( k > LSF_COS_TAB_SZ_FIX ) {
                i++;
                if( i > MAX_ITERATIONS_A2NLSF_FIX ) {
                    
                    NLSF[ 0 ] = (opus_int16)silk_DIV32_16( 1 << 15, d + 1 );
                    for( k = 1; k < d; k++ ) {
                        NLSF[ k ] = (opus_int16)silk_ADD16( NLSF[ k-1 ], NLSF[ 0 ] );
                    }
                    return;
                }

            
                silk_bwexpander_32( a_Q16, d, 65536 - silk_LSHIFT( 1, i ) );

                silk_A2NLSF_init( a_Q16, P, Q, dd );
                p = P;                            
                xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
                ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                if( ylo < 0 ) {
                    
                    NLSF[ 0 ] = 0;
                    p = Q;                     
                    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                    root_ix = 1;                
                } else {
                    root_ix = 0;                 
                }
                k = 1;                      
            }
        }
    }
}
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "SigProc_FIX.h"
#include "tables.h"

#define BIN_DIV_STEPS_A2NLSF_FIX      3 
#define MAX_ITERATIONS_A2NLSF_FIX    16


static OPUS_INLINE void silk_A2NLSF_trans_poly(
    opus_int32          *p,                    
    const opus_int      dd                      
)
{
    opus_int k, n;

    for( k = 2; k <= dd; k++ ) {
        for( n = dd; n > k; n-- ) {
            p[ n - 2 ] -= p[ n ];
        }
        p[ k - 2 ] -= silk_LSHIFT( p[ k ], 1 );
    }
}

static OPUS_INLINE opus_int32 silk_A2NLSF_eval_poly( 
    opus_int32          *p,                    
    const opus_int32    x,                     
    const opus_int      dd                     
)
{
    opus_int   n;
    opus_int32 x_Q16, y32;

    y32 = p[ dd ];                                  /* Q16 */
    x_Q16 = silk_LSHIFT( x, 4 );

    if ( opus_likely( 8 == dd ) )
    {
        y32 = silk_SMLAWW( p[ 7 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 6 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 5 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 4 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 3 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 2 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 1 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 0 ], y32, x_Q16 );
    }
    else
    {
        for( n = dd - 1; n >= 0; n-- ) {
            y32 = silk_SMLAWW( p[ n ], y32, x_Q16 );    /* Q16 */
        }
    }
    return y32;
}

static OPUS_INLINE void silk_A2NLSF_init(
     const opus_int32    *a_Q16,
     opus_int32          *P,
     opus_int32          *Q,
     const opus_int      dd
)
{
    opus_int k;

   
    P[dd] = silk_LSHIFT( 1, 16 );
    Q[dd] = silk_LSHIFT( 1, 16 );
    for( k = 0; k < dd; k++ ) {
        P[ k ] = -a_Q16[ dd - k - 1 ] - a_Q16[ dd + k ];    /* Q16 */
        Q[ k ] = -a_Q16[ dd - k - 1 ] + a_Q16[ dd + k ];    /* Q16 */
    }


    for( k = dd; k > 0; k-- ) {
        P[ k - 1 ] -= P[ k ];
        Q[ k - 1 ] += Q[ k ];
    }

    
    silk_A2NLSF_trans_poly( P, dd );
    silk_A2NLSF_trans_poly( Q, dd );
}


void silk_A2NLSF(
    opus_int16                  *NLSF,              
    opus_int32                  *a_Q16,            
    const opus_int              d                   
)
{
    opus_int   i, k, m, dd, root_ix, ffrac;
    opus_int32 xlo, xhi, xmid;
    opus_int32 ylo, yhi, ymid, thr;
    opus_int32 nom, den;
    opus_int32 P[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 Q[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 *PQ[ 2 ];
    opus_int32 *p;

    
    PQ[ 0 ] = P;
    PQ[ 1 ] = Q;

    dd = silk_RSHIFT( d, 1 );

    silk_A2NLSF_init( a_Q16, P, Q, dd );

    
    p = P;                          

    xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );

    if( ylo < 0 ) {
        */
        NLSF[ 0 ] = 0;
        p = Q;                      
        ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
        root_ix = 1;                
    } else {
        root_ix = 0;            
    }
    k = 1;                          
    i = 0;                         
    thr = 0;
    while( 1 ) {
        
        xhi = silk_LSFCosTab_FIX_Q12[ k ]; /* Q12 */
        yhi = silk_A2NLSF_eval_poly( p, xhi, dd );

        
        if( ( ylo <= 0 && yhi >= thr ) || ( ylo >= 0 && yhi <= -thr ) ) {
            if( yhi == 0 ) {
              
              
                thr = 1;
            } else {
                thr = 0;
            }
           
            ffrac = -256;
            for( m = 0; m < BIN_DIV_STEPS_A2NLSF_FIX; m++ ) {
                /* Evaluate polynomial */
                xmid = silk_RSHIFT_ROUND( xlo + xhi, 1 );
                ymid = silk_A2NLSF_eval_poly( p, xmid, dd );

                
                if( ( ylo <= 0 && ymid >= 0 ) || ( ylo >= 0 && ymid <= 0 ) ) {
                    
                    xhi = xmid;
                    yhi = ymid;
                } else {
                    
                    xlo = xmid;
                    ylo = ymid;
                    ffrac = silk_ADD_RSHIFT( ffrac, 128, m );
                }
            }

            
            if( silk_abs( ylo ) < 65536 ) {
               
                den = ylo - yhi;
                nom = silk_LSHIFT( ylo, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) + silk_RSHIFT( den, 1 );
                if( den != 0 ) {
                    ffrac += silk_DIV32( nom, den );
                }
            } else {
                
                ffrac += silk_DIV32( ylo, silk_RSHIFT( ylo - yhi, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) );
            }
            NLSF[ root_ix ] = (opus_int16)silk_min_32( silk_LSHIFT( (opus_int32)k, 8 ) + ffrac, silk_int16_MAX );

            silk_assert( NLSF[ root_ix ] >= 0 );

            root_ix++;        
            if( root_ix >= d ) {
               
                break;
            }
            /* Alternate pointer to polynomial */
            p = PQ[ root_ix & 1 ];

            /
            xlo = silk_LSFCosTab_FIX_Q12[ k - 1 ]; /* Q12*/
            ylo = silk_LSHIFT( 1 - ( root_ix & 2 ), 12 );
        } else {
            
            k++;
            xlo = xhi;
            ylo = yhi;
            thr = 0;

            if( k > LSF_COS_TAB_SZ_FIX ) {
                i++;
                if( i > MAX_ITERATIONS_A2NLSF_FIX ) {
                    
                    NLSF[ 0 ] = (opus_int16)silk_DIV32_16( 1 << 15, d + 1 );
                    for( k = 1; k < d; k++ ) {
                        NLSF[ k ] = (opus_int16)silk_ADD16( NLSF[ k-1 ], NLSF[ 0 ] );
                    }
                    return;
                }

            
                silk_bwexpander_32( a_Q16, d, 65536 - silk_LSHIFT( 1, i ) );

                silk_A2NLSF_init( a_Q16, P, Q, dd );
                p = P;                            
                xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
                ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                if( ylo < 0 ) {
                    
                    NLSF[ 0 ] = 0;
                    p = Q;                     
                    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                    root_ix = 1;                
                } else {
                    root_ix = 0;                 
                }
                k = 1;                      
            }
        }
    }
}
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "SigProc_FIX.h"
#include "tables.h"

#define BIN_DIV_STEPS_A2NLSF_FIX      3 
#define MAX_ITERATIONS_A2NLSF_FIX    16


static OPUS_INLINE void silk_A2NLSF_trans_poly(
    opus_int32          *p,                    
    const opus_int      dd                      
)
{
    opus_int k, n;

    for( k = 2; k <= dd; k++ ) {
        for( n = dd; n > k; n-- ) {
            p[ n - 2 ] -= p[ n ];
        }
        p[ k - 2 ] -= silk_LSHIFT( p[ k ], 1 );
    }
}

static OPUS_INLINE opus_int32 silk_A2NLSF_eval_poly( 
    opus_int32          *p,                    
    const opus_int32    x,                     
    const opus_int      dd                     
)
{
    opus_int   n;
    opus_int32 x_Q16, y32;

    y32 = p[ dd ];                                  /* Q16 */
    x_Q16 = silk_LSHIFT( x, 4 );

    if ( opus_likely( 8 == dd ) )
    {
        y32 = silk_SMLAWW( p[ 7 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 6 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 5 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 4 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 3 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 2 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 1 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 0 ], y32, x_Q16 );
    }
    else
    {
        for( n = dd - 1; n >= 0; n-- ) {
            y32 = silk_SMLAWW( p[ n ], y32, x_Q16 );    /* Q16 */
        }
    }
    return y32;
}

static OPUS_INLINE void silk_A2NLSF_init(
     const opus_int32    *a_Q16,
     opus_int32          *P,
     opus_int32          *Q,
     const opus_int      dd
)
{
    opus_int k;

   
    P[dd] = silk_LSHIFT( 1, 16 );
    Q[dd] = silk_LSHIFT( 1, 16 );
    for( k = 0; k < dd; k++ ) {
        P[ k ] = -a_Q16[ dd - k - 1 ] - a_Q16[ dd + k ];    /* Q16 */
        Q[ k ] = -a_Q16[ dd - k - 1 ] + a_Q16[ dd + k ];    /* Q16 */
    }


    for( k = dd; k > 0; k-- ) {
        P[ k - 1 ] -= P[ k ];
        Q[ k - 1 ] += Q[ k ];
    }

    
    silk_A2NLSF_trans_poly( P, dd );
    silk_A2NLSF_trans_poly( Q, dd );
}


void silk_A2NLSF(
    opus_int16                  *NLSF,              
    opus_int32                  *a_Q16,            
    const opus_int              d                   
)
{
    opus_int   i, k, m, dd, root_ix, ffrac;
    opus_int32 xlo, xhi, xmid;
    opus_int32 ylo, yhi, ymid, thr;
    opus_int32 nom, den;
    opus_int32 P[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 Q[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 *PQ[ 2 ];
    opus_int32 *p;

    
    PQ[ 0 ] = P;
    PQ[ 1 ] = Q;

    dd = silk_RSHIFT( d, 1 );

    silk_A2NLSF_init( a_Q16, P, Q, dd );

    
    p = P;                          

    xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );

    if( ylo < 0 ) {
        */
        NLSF[ 0 ] = 0;
        p = Q;                      
        ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
        root_ix = 1;                
    } else {
        root_ix = 0;            
    }
    k = 1;                          
    i = 0;                         
    thr = 0;
    while( 1 ) {
        
        xhi = silk_LSFCosTab_FIX_Q12[ k ]; /* Q12 */
        yhi = silk_A2NLSF_eval_poly( p, xhi, dd );

        
        if( ( ylo <= 0 && yhi >= thr ) || ( ylo >= 0 && yhi <= -thr ) ) {
            if( yhi == 0 ) {
              
              
                thr = 1;
            } else {
                thr = 0;
            }
           
            ffrac = -256;
            for( m = 0; m < BIN_DIV_STEPS_A2NLSF_FIX; m++ ) {
                /* Evaluate polynomial */
                xmid = silk_RSHIFT_ROUND( xlo + xhi, 1 );
                ymid = silk_A2NLSF_eval_poly( p, xmid, dd );

                
                if( ( ylo <= 0 && ymid >= 0 ) || ( ylo >= 0 && ymid <= 0 ) ) {
                    
                    xhi = xmid;
                    yhi = ymid;
                } else {
                    
                    xlo = xmid;
                    ylo = ymid;
                    ffrac = silk_ADD_RSHIFT( ffrac, 128, m );
                }
            }

            
            if( silk_abs( ylo ) < 65536 ) {
               
                den = ylo - yhi;
                nom = silk_LSHIFT( ylo, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) + silk_RSHIFT( den, 1 );
                if( den != 0 ) {
                    ffrac += silk_DIV32( nom, den );
                }
            } else {
                
                ffrac += silk_DIV32( ylo, silk_RSHIFT( ylo - yhi, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) );
            }
            NLSF[ root_ix ] = (opus_int16)silk_min_32( silk_LSHIFT( (opus_int32)k, 8 ) + ffrac, silk_int16_MAX );

            silk_assert( NLSF[ root_ix ] >= 0 );

            root_ix++;        
            if( root_ix >= d ) {
               
                break;
            }
            /* Alternate pointer to polynomial */
            p = PQ[ root_ix & 1 ];

            /
            xlo = silk_LSFCosTab_FIX_Q12[ k - 1 ]; /* Q12*/
            ylo = silk_LSHIFT( 1 - ( root_ix & 2 ), 12 );
        } else {
            
            k++;
            xlo = xhi;
            ylo = yhi;
            thr = 0;

            if( k > LSF_COS_TAB_SZ_FIX ) {
                i++;
                if( i > MAX_ITERATIONS_A2NLSF_FIX ) {
                    
                    NLSF[ 0 ] = (opus_int16)silk_DIV32_16( 1 << 15, d + 1 );
                    for( k = 1; k < d; k++ ) {
                        NLSF[ k ] = (opus_int16)silk_ADD16( NLSF[ k-1 ], NLSF[ 0 ] );
                    }
                    return;
                }

            
                silk_bwexpander_32( a_Q16, d, 65536 - silk_LSHIFT( 1, i ) );

                silk_A2NLSF_init( a_Q16, P, Q, dd );
                p = P;                            
                xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
                ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                if( ylo < 0 ) {
                    
                    NLSF[ 0 ] = 0;
                    p = Q;                     
                    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                    root_ix = 1;                
                } else {
                    root_ix = 0;                 
                }
                k = 1;                      
            }
        }
    }
}
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "SigProc_FIX.h"
#include "tables.h"

#define BIN_DIV_STEPS_A2NLSF_FIX      3 
#define MAX_ITERATIONS_A2NLSF_FIX    16


static OPUS_INLINE void silk_A2NLSF_trans_poly(
    opus_int32          *p,                    
    const opus_int      dd                      
)
{
    opus_int k, n;

    for( k = 2; k <= dd; k++ ) {
        for( n = dd; n > k; n-- ) {
            p[ n - 2 ] -= p[ n ];
        }
        p[ k - 2 ] -= silk_LSHIFT( p[ k ], 1 );
    }
}

static OPUS_INLINE opus_int32 silk_A2NLSF_eval_poly( 
    opus_int32          *p,                    
    const opus_int32    x,                     
    const opus_int      dd                     
)
{
    opus_int   n;
    opus_int32 x_Q16, y32;

    y32 = p[ dd ];                                  /* Q16 */
    x_Q16 = silk_LSHIFT( x, 4 );

    if ( opus_likely( 8 == dd ) )
    {
        y32 = silk_SMLAWW( p[ 7 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 6 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 5 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 4 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 3 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 2 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 1 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 0 ], y32, x_Q16 );
    }
    else
    {
        for( n = dd - 1; n >= 0; n-- ) {
            y32 = silk_SMLAWW( p[ n ], y32, x_Q16 );    /* Q16 */
        }
    }
    return y32;
}

static OPUS_INLINE void silk_A2NLSF_init(
     const opus_int32    *a_Q16,
     opus_int32          *P,
     opus_int32          *Q,
     const opus_int      dd
)
{
    opus_int k;

   
    P[dd] = silk_LSHIFT( 1, 16 );
    Q[dd] = silk_LSHIFT( 1, 16 );
    for( k = 0; k < dd; k++ ) {
        P[ k ] = -a_Q16[ dd - k - 1 ] - a_Q16[ dd + k ];    /* Q16 */
        Q[ k ] = -a_Q16[ dd - k - 1 ] + a_Q16[ dd + k ];    /* Q16 */
    }


    for( k = dd; k > 0; k-- ) {
        P[ k - 1 ] -= P[ k ];
        Q[ k - 1 ] += Q[ k ];
    }

    
    silk_A2NLSF_trans_poly( P, dd );
    silk_A2NLSF_trans_poly( Q, dd );
}


void silk_A2NLSF(
    opus_int16                  *NLSF,              
    opus_int32                  *a_Q16,            
    const opus_int              d                   
)
{
    opus_int   i, k, m, dd, root_ix, ffrac;
    opus_int32 xlo, xhi, xmid;
    opus_int32 ylo, yhi, ymid, thr;
    opus_int32 nom, den;
    opus_int32 P[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 Q[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 *PQ[ 2 ];
    opus_int32 *p;

    
    PQ[ 0 ] = P;
    PQ[ 1 ] = Q;

    dd = silk_RSHIFT( d, 1 );

    silk_A2NLSF_init( a_Q16, P, Q, dd );

    
    p = P;                          

    xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );

    if( ylo < 0 ) {
        */
        NLSF[ 0 ] = 0;
        p = Q;                      
        ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
        root_ix = 1;                
    } else {
        root_ix = 0;            
    }
    k = 1;                          
    i = 0;                         
    thr = 0;
    while( 1 ) {
        
        xhi = silk_LSFCosTab_FIX_Q12[ k ]; /* Q12 */
        yhi = silk_A2NLSF_eval_poly( p, xhi, dd );

        
        if( ( ylo <= 0 && yhi >= thr ) || ( ylo >= 0 && yhi <= -thr ) ) {
            if( yhi == 0 ) {
              
              
                thr = 1;
            } else {
                thr = 0;
            }
           
            ffrac = -256;
            for( m = 0; m < BIN_DIV_STEPS_A2NLSF_FIX; m++ ) {
                /* Evaluate polynomial */
                xmid = silk_RSHIFT_ROUND( xlo + xhi, 1 );
                ymid = silk_A2NLSF_eval_poly( p, xmid, dd );

                
                if( ( ylo <= 0 && ymid >= 0 ) || ( ylo >= 0 && ymid <= 0 ) ) {
                    
                    xhi = xmid;
                    yhi = ymid;
                } else {
                    
                    xlo = xmid;
                    ylo = ymid;
                    ffrac = silk_ADD_RSHIFT( ffrac, 128, m );
                }
            }

            
            if( silk_abs( ylo ) < 65536 ) {
               
                den = ylo - yhi;
                nom = silk_LSHIFT( ylo, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) + silk_RSHIFT( den, 1 );
                if( den != 0 ) {
                    ffrac += silk_DIV32( nom, den );
                }
            } else {
                
                ffrac += silk_DIV32( ylo, silk_RSHIFT( ylo - yhi, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) );
            }
            NLSF[ root_ix ] = (opus_int16)silk_min_32( silk_LSHIFT( (opus_int32)k, 8 ) + ffrac, silk_int16_MAX );

            silk_assert( NLSF[ root_ix ] >= 0 );

            root_ix++;        
            if( root_ix >= d ) {
               
                break;
            }
            /* Alternate pointer to polynomial */
            p = PQ[ root_ix & 1 ];

            /
            xlo = silk_LSFCosTab_FIX_Q12[ k - 1 ]; /* Q12*/
            ylo = silk_LSHIFT( 1 - ( root_ix & 2 ), 12 );
        } else {
            
            k++;
            xlo = xhi;
            ylo = yhi;
            thr = 0;

            if( k > LSF_COS_TAB_SZ_FIX ) {
                i++;
                if( i > MAX_ITERATIONS_A2NLSF_FIX ) {
                    
                    NLSF[ 0 ] = (opus_int16)silk_DIV32_16( 1 << 15, d + 1 );
                    for( k = 1; k < d; k++ ) {
                        NLSF[ k ] = (opus_int16)silk_ADD16( NLSF[ k-1 ], NLSF[ 0 ] );
                    }
                    return;
                }

            
                silk_bwexpander_32( a_Q16, d, 65536 - silk_LSHIFT( 1, i ) );

                silk_A2NLSF_init( a_Q16, P, Q, dd );
                p = P;                            
                xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
                ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                if( ylo < 0 ) {
                    
                    NLSF[ 0 ] = 0;
                    p = Q;                     
                    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                    root_ix = 1;                
                } else {
                    root_ix = 0;                 
                }
                k = 1;                      
            }
        }
    }
}
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "SigProc_FIX.h"
#include "tables.h"

#define BIN_DIV_STEPS_A2NLSF_FIX      3 
#define MAX_ITERATIONS_A2NLSF_FIX    16


static OPUS_INLINE void silk_A2NLSF_trans_poly(
    opus_int32          *p,                    
    const opus_int      dd                      
)
{
    opus_int k, n;

    for( k = 2; k <= dd; k++ ) {
        for( n = dd; n > k; n-- ) {
            p[ n - 2 ] -= p[ n ];
        }
        p[ k - 2 ] -= silk_LSHIFT( p[ k ], 1 );
    }
}

static OPUS_INLINE opus_int32 silk_A2NLSF_eval_poly( 
    opus_int32          *p,                    
    const opus_int32    x,                     
    const opus_int      dd                     
)
{
    opus_int   n;
    opus_int32 x_Q16, y32;

    y32 = p[ dd ];                                  /* Q16 */
    x_Q16 = silk_LSHIFT( x, 4 );

    if ( opus_likely( 8 == dd ) )
    {
        y32 = silk_SMLAWW( p[ 7 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 6 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 5 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 4 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 3 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 2 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 1 ], y32, x_Q16 );
        y32 = silk_SMLAWW( p[ 0 ], y32, x_Q16 );
    }
    else
    {
        for( n = dd - 1; n >= 0; n-- ) {
            y32 = silk_SMLAWW( p[ n ], y32, x_Q16 );    /* Q16 */
        }
    }
    return y32;
}

static OPUS_INLINE void silk_A2NLSF_init(
     const opus_int32    *a_Q16,
     opus_int32          *P,
     opus_int32          *Q,
     const opus_int      dd
)
{
    opus_int k;

   
    P[dd] = silk_LSHIFT( 1, 16 );
    Q[dd] = silk_LSHIFT( 1, 16 );
    for( k = 0; k < dd; k++ ) {
        P[ k ] = -a_Q16[ dd - k - 1 ] - a_Q16[ dd + k ];    /* Q16 */
        Q[ k ] = -a_Q16[ dd - k - 1 ] + a_Q16[ dd + k ];    /* Q16 */
    }


    for( k = dd; k > 0; k-- ) {
        P[ k - 1 ] -= P[ k ];
        Q[ k - 1 ] += Q[ k ];
    }

    
    silk_A2NLSF_trans_poly( P, dd );
    silk_A2NLSF_trans_poly( Q, dd );
}


void silk_A2NLSF(
    opus_int16                  *NLSF,              
    opus_int32                  *a_Q16,            
    const opus_int              d                   
)
{
    opus_int   i, k, m, dd, root_ix, ffrac;
    opus_int32 xlo, xhi, xmid;
    opus_int32 ylo, yhi, ymid, thr;
    opus_int32 nom, den;
    opus_int32 P[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 Q[ SILK_MAX_ORDER_LPC / 2 + 1 ];
    opus_int32 *PQ[ 2 ];
    opus_int32 *p;

    
    PQ[ 0 ] = P;
    PQ[ 1 ] = Q;

    dd = silk_RSHIFT( d, 1 );

    silk_A2NLSF_init( a_Q16, P, Q, dd );

    
    p = P;                          

    xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );

    if( ylo < 0 ) {
        */
        NLSF[ 0 ] = 0;
        p = Q;                      
        ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
        root_ix = 1;                
    } else {
        root_ix = 0;            
    }
    k = 1;                          
    i = 0;                         
    thr = 0;
    while( 1 ) {
        
        xhi = silk_LSFCosTab_FIX_Q12[ k ]; /* Q12 */
        yhi = silk_A2NLSF_eval_poly( p, xhi, dd );

        
        if( ( ylo <= 0 && yhi >= thr ) || ( ylo >= 0 && yhi <= -thr ) ) {
            if( yhi == 0 ) {
              
              
                thr = 1;
            } else {
                thr = 0;
            }
           
            ffrac = -256;
            for( m = 0; m < BIN_DIV_STEPS_A2NLSF_FIX; m++ ) {
                /* Evaluate polynomial */
                xmid = silk_RSHIFT_ROUND( xlo + xhi, 1 );
                ymid = silk_A2NLSF_eval_poly( p, xmid, dd );

                
                if( ( ylo <= 0 && ymid >= 0 ) || ( ylo >= 0 && ymid <= 0 ) ) {
                    
                    xhi = xmid;
                    yhi = ymid;
                } else {
                    
                    xlo = xmid;
                    ylo = ymid;
                    ffrac = silk_ADD_RSHIFT( ffrac, 128, m );
                }
            }

            
            if( silk_abs( ylo ) < 65536 ) {
               
                den = ylo - yhi;
                nom = silk_LSHIFT( ylo, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) + silk_RSHIFT( den, 1 );
                if( den != 0 ) {
                    ffrac += silk_DIV32( nom, den );
                }
            } else {
                
                ffrac += silk_DIV32( ylo, silk_RSHIFT( ylo - yhi, 8 - BIN_DIV_STEPS_A2NLSF_FIX ) );
            }
            NLSF[ root_ix ] = (opus_int16)silk_min_32( silk_LSHIFT( (opus_int32)k, 8 ) + ffrac, silk_int16_MAX );

            silk_assert( NLSF[ root_ix ] >= 0 );

            root_ix++;        
            if( root_ix >= d ) {
               
                break;
            }
            /* Alternate pointer to polynomial */
            p = PQ[ root_ix & 1 ];

            /
            xlo = silk_LSFCosTab_FIX_Q12[ k - 1 ]; /* Q12*/
            ylo = silk_LSHIFT( 1 - ( root_ix & 2 ), 12 );
        } else {
            
            k++;
            xlo = xhi;
            ylo = yhi;
            thr = 0;

            if( k > LSF_COS_TAB_SZ_FIX ) {
                i++;
                if( i > MAX_ITERATIONS_A2NLSF_FIX ) {
                    
                    NLSF[ 0 ] = (opus_int16)silk_DIV32_16( 1 << 15, d + 1 );
                    for( k = 1; k < d; k++ ) {
                        NLSF[ k ] = (opus_int16)silk_ADD16( NLSF[ k-1 ], NLSF[ 0 ] );
                    }
                    return;
                }

            
                silk_bwexpander_32( a_Q16, d, 65536 - silk_LSHIFT( 1, i ) );

                silk_A2NLSF_init( a_Q16, P, Q, dd );
                p = P;                            
                xlo = silk_LSFCosTab_FIX_Q12[ 0 ]; /* Q12*/
                ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                if( ylo < 0 ) {
                    
                    NLSF[ 0 ] = 0;
                    p = Q;                     
                    ylo = silk_A2NLSF_eval_poly( p, xlo, dd );
                    root_ix = 1;                
                } else {
                    root_ix = 0;                 
                }
                k = 1;                      
            }
        }
    }
}
