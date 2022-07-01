"""
Author: suegdu | suegdu Industries
Source: https://github.com/suegdu/NT-RTE
Github: https://github.com/suegdu/NT-RTE
The main function are written under this file NT234.py
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
from Subx import NTBackgourndmgr
import time
from Subx import NTCrashHandler
print("Loading RTE....")
print("...............")
print("Importing Site-Packages.....")
try:
 import os
 os.system("title Loading System Files....")
 from pathlib import Path
 from datetime import datetime
 import wmi
 import sys
 import platform
 from colorama import Fore, Back, Style,init
 from threading import Thread
 import requests
 print("Done.")
except:
    print("Error: Something Went Wrong While Importing Site-Packages")
    time.sleep(1)
    NTCrashHandler.importinghandler()
print("Importing Subx Packages....")
try:
 from Subx import SubxDH
 from Subx import SubxUSV
 from Subx import SubxUSVnull
 from Subx import SubxDTI
 from Subx import SubxSTM
 from Subx import Subxccf
 print("Done.")
except:
    print("Error: Something Went Wrong While Importing Packages")
    time.sleep(2)
    NTCrashHandler.importinghandler()
print("Importing NT Classes....")
try:
   from Subx import NTUpdater
   from Subx import NTLogger
   from Subx import NTFilemgr 
   from Subx import NTOutsysmgr
   from Subx import NTBackgourndmgr
except: 
    print("Error: Something Went Wrong While Importing Packages")
    time.sleep(2)
    NTCrashHandler.importinghandler()
try:
    from Subx import NTNetworkmgr
    offlinerender:bool = False
except requests.exceptions.ConnectionError:
    print()
    print("Error: Unable to establish a valid connection. NT will start on the offline mode.")
    offlinerender:bool = True
    
    time.sleep(2)
except:
    print("Error: Something Went Wrong While Importing Packages")
    time.sleep(2)
    NTCrashHandler.importinghandler()
__NTversion__ = "NT 1.2.5"
with open("./veri.NT","a") as file:
    file.write("Do not delete this file. Thank you]\n\n000009")
a = os.path.exists("./veri.NT")
if a == True:
    pass
elif a == False:
 try:
     os.chdir("../")
     os.remove("./NT0Installer.py")
     print("Apparently you ran NT for the first time, Please re open NT again to apply some changes. Close NT")
 except FileNotFoundError:
     pass
class MemoryPointers:
    class Msgs:
     Helpmsg_GN = str(f"""
The current state of available commands:

- usv | {SubxUSV.__basedversion__}
Scans for the giving username on more than 350 sites around internet (Sites are being updated usually)

- dh | {SubxDH.__version__}\nDisplays several information about the giving hostname.

- dti | {SubxDTI.__version__} (Third Party Program)\nExtract useful information from a single users Discord authorization token.

- stm | {SubxSTM.__version__}\nCreates a grabbing file that Grabs several information from the machine that runs the following script through a Discord Webhook.

- fcc | null\nGenerates a random fake credit card information.

- netstats | null\nDisplays the current connections on your machine.

- ntout | null\nEcho.

- update | null\n Checks for an update and install it for NT.

- outs | null\nExecuting a command from the local machine's terminal.
\n
For its usage use ?[command]""")

     DHmsg_help = str("Usage:\n- dh [Press Enter]\n- dh [Hostname]")
     
     USVmsg_help = str("Usage:\n- usv [Press Enter]\n- usv [Username] [Mode]\n\n- (Modes: 1 = Full Scan. | 2 = Only Popular Sites Scan.)")
     netstsmsg_help = str("Usage:\n- netstats")
     dtimsg_help = str("Usage:\n- dti [Press Enter]\n- dti [Token]")
     stmmsg_help = str("Usage:\n- stm [Press Enter]\n- stm [File name] [Valid Discord Webhook Link]")

     ntoutmsg_help = str("Usage:\n- ntout [message]")
     outsmsg_help = str("Usage:\n- outs [command*]")
     fccmsg_help = str("Usage:\n- fcc [Press Enter]")
     upmsg_help = str("Usage:\n- update [Press Enter]")
    class Lists:
        verList:str = ("ver","v","version")
        clearList:str = ("clear","cls","clean")
    class Logging:
        warning:str = "WARNING"
        info:str = "INFO"
        awaiting:str = "AWAITING"
        crash:str = "ERROR"
        name:str = "NTLogs"
        startupmsg = str("Loaded all classes. Starting NT....")
        success = str("Loaded.")
        NTCrashed = str("NT Has just crashed. (Passed the main line into the crash rail x099937)")
        offlinemode = str("Error: Unable to establish a valid connection. NT will start on the offline mode. (Probabl point the NTNetworkmgr class wont be loaded. you might need to restart NT to establish a connection again, or just by retrying the procedure of your need)")



NTLogger.Program.NTLog(name=MemoryPointers.Logging.name,liter="Memory",level=MemoryPointers.Logging.info,content=MemoryPointers.Logging.startupmsg,f=__file__,v=__NTversion__)
if offlinerender == False:
    pass
elif offlinerender == True:
    NTLogger.Program.NTLog(name=MemoryPointers.Logging.name,liter="Memory",level=MemoryPointers.Logging.warning,content=MemoryPointers.Logging.offlinemode,f=__file__,v=__NTversion__)
NTLogger.Program.NTLog(name=MemoryPointers.Logging.name,liter="Memory",level=MemoryPointers.Logging.info,content=MemoryPointers.Logging.success,f=__file__,v=__NTversion__)
os.system("cls")
init(autoreset=True)
NTBackgourndmgr.th0 = True
NTBackgourndmgr.th1 = True
NTBackgourndmgr.th2 = True
Thread(target=NTBackgourndmgr.Consolehosttitle).start()
Thread(target=NTBackgourndmgr.NTTempfixer).start()
Thread(target=NTBackgourndmgr.NTBackgroundupdates).start()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
rst = Style.RESET_ALL
c = wmi.WMI()   
__github__ = "https://github.com/suegdu/NT-RTE"
my_system = c.Win32_ComputerSystem()[0]










def EH_return(liter,version=None,f=None,exceptTr=None,command=None):
        """The error handler of NT.(returner)"""
        if liter=="occ":
            print(f"[{f}] [{version}] Error: an error was occurred: {exceptTr}")
        elif liter=="nvu":
            print(f"Error: Not a valid command usage. For help use ?{command}")
def NTversion():
    print(f" {__NTversion__}")
    print(f" {sys.argv[0]}")
    print(f" {__github__}")
    print(f" {platform.platform()} {platform.node()}")
    print()
def substring_after(s, delim):
    return s.partition(delim)[2]
def NTmainorating():
   NTversion()
   NTmainforming()
def NTosdisplay():
    print(f"{platform.platform()} {platform.node()}")
def NTnullveildOut(call):
    print(str(call))
def NTscreenmgr(liter):
    if liter=="clear":
        os.system("cls")
        NTreturn(mode="return")
    elif liter=="crash-N":
        NTCrashHandler.handler()
def NTexit():
    print("\rExiting Procedure in: 2",end="")
    time.sleep(1)
    print("\rExiting Procedure in: 1",end="")
    time.sleep(1)
    print("\rExiting Procedure in: 0")
    os.kill(os.getpid(), 9)
def NThelpreturn(liter):
    if liter=="dh":
        print(MemoryPointers.Msgs.DHmsg_help)
        NTreturn(mode="memoryreturn")
    elif liter=="GN":
        print(MemoryPointers.Msgs.Helpmsg_GN)
        NTreturn(mode="memoryreturn")
    elif liter=="usv":
        print(MemoryPointers.Msgs.USVmsg_help)
        NTreturn("memoryreturn")
    elif liter=="ntout":
        print(MemoryPointers.Msgs.ntoutmsg_help)
        NTreturn("memoryreturn")
    elif liter=="netstats":
        print(MemoryPointers.Msgs.netstsmsg_help)
        NTreturn("memoryreturn")
    elif liter=="outs":
        print(MemoryPointers.Msgs.outsmsg_help)
        NTreturn("memoryreturn")
    elif liter=="dti":
        print(MemoryPointers.Msgs.dtimsg_help)
        NTreturn("memoryreturn")
    elif liter=="stm":
        print(MemoryPointers.Msgs.stmmsg_help)
        NTreturn("memoryreturn")
    elif liter=="fcc":
        print(MemoryPointers.Msgs.fccmsg_help)
        NTreturn("memoryreturn")
    elif liter=="update":
        print(MemoryPointers.Msgs.upmsg_help)
        NTreturn("memoryreturn")
def NTreturn(mode):
    if mode=="memoryreturn":
        print()
        NTmainforming()
    elif mode=="return":
        NTmainorating()
def NTmainforming():
   print(f"{Fore.LIGHTYELLOW_EX}[NT]:> ",end="")
   forming_input = input().lower()
   if forming_input=="os":
       NTosdisplay()
       NTreturn(mode="memoryreturn")
   elif forming_input=="":
       NTreturn(mode="memoryreturn")
   elif forming_input=="exit":
       NTexit()
   elif forming_input=="e":
       NTexit()
   elif forming_input.startswith(" "):
       NTreturn(mode="memoryreturn")
   elif forming_input=="dir":
       os.system("dir")
       NTreturn(mode="memoryreturn")
   elif forming_input=="dh":
    SubxDH.Program.main()
    NTreturn(mode="memoryreturn")
   elif forming_input=="ls":
       os.system("dir")
       NTreturn(mode="memoryreturn")
   elif forming_input=="start":
    os.startfile(__file__)
    NTreturn("memoryreturn")
   elif forming_input.startswith("ntout"):
    NTnullveildOut(call=str(substring_after(forming_input,forming_input.split()[0])))
    NTreturn(mode="memoryreturn")

   elif forming_input.startswith("dh"):
    try:
     SubxDH.Program.Submain(hostname=forming_input.split()[1])
     NTreturn(mode="memoryreturn")
    except IndexError:
        EH_return(liter="nvu",command="dh")
        NTreturn(mode="memoryreturn")
   elif forming_input.startswith("outs"):
    NTOutsysmgr.Program.systemcall(substring_after(forming_input,forming_input.split()[0]))
    NTreturn(mode="memoryreturn")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="dh":
    NThelpreturn(liter="dh")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="usv":
    NThelpreturn(liter="usv")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="ntout":
    NThelpreturn(liter="ntout")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="outs":
    NThelpreturn(liter="outs")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="dti":
    NThelpreturn(liter="dti")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="stm":
    NThelpreturn(liter="stm")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="fcc":
    NThelpreturn(liter="fcc")
   elif forming_input.startswith("?") and forming_input.replace("?","")=="update":
    NThelpreturn(liter="update")
   elif forming_input=="stm":
    SubxSTM.Program.main2()
    NTreturn("memoryreturn")
   elif forming_input.startswith("stm"):
    SubxSTM.Program.main(F_name=forming_input.split()[1],ST_webhook=forming_input.split()[2])
    NTreturn("memoryreturn")
   elif forming_input=="dti":
    SubxDTI.main2()
    NTreturn("memoryreturn")
   elif forming_input.startswith("dti"):
    try:
        SubxDTI.main(token=forming_input.split()[1])
        NTreturn("memoryreturn")
    except:
        EH_return(liter="nvu",command="dti")
        NTreturn("memoryreturn")
   
   elif forming_input.startswith("?"):
    NThelpreturn(liter="GN")
   elif forming_input in MemoryPointers.Lists.clearList:
    NTscreenmgr(liter="clear") 
   elif forming_input in MemoryPointers.Lists.verList:
    NTversion()
    NTreturn("memoryreturn")
   elif forming_input=="pubip":
    print(NTNetworkmgr.MemoryPointers.Publicinternetprotocol)
    NTreturn("memoryreturn")
   elif forming_input=="netstats":
    try:
     NTNetworkmgr.Program.ETC.localingAC()   
     NTreturn("memoryreturn")
    except:
        EH_return(liter="occ",version=__NTversion__,f=__file__,exceptTr="Unknown Error")
        NTreturn("memoryreturn")
   elif forming_input=="usv":
    SubxUSV.mainputtes()
    NTreturn("memoryreturn")
   elif forming_input=="update":
    NTUpdater.main()
    if NTUpdater.vail== True:
     try:
      os._exit(0)
     except:
         raise SystemError
    elif NTUpdater.vail== False:
        NTreturn("memoryreturn")
   elif forming_input=="fcc":
    Subxccf.Program.main()
    NTreturn("memoryreturn")
   elif forming_input.startswith("usv"):
    try:
        SubxUSVnull.mainputtes(validusnmae=forming_input.split()[1],validsel=forming_input.split()[2])
        NTreturn("memoryreturn")
    except:
        EH_return(liter="nvu",command="usv")
        NTreturn("memoryreturn")
   else:
        print(f"'{forming_input}' is not recognizable by NT as an internal command. or operable program for NT")
        print()
        NTmainforming()

    
       

if NTUpdater.vail== True:
    exit(0)
elif NTUpdater.vail == False:
 NTLogger.Program.NTLog(name=MemoryPointers.Logging.name,liter="Memory",level=MemoryPointers.Logging.info,content="Started.",f=__file__,v=__NTversion__)
 NTmainorating()
 if NTUpdater.vail== True:
    print()
    
 elif NTUpdater.vail == False:
  NTLogger.Program.NTLog(name=MemoryPointers.Logging.name,liter="Memory",level=MemoryPointers.Logging.crash,content=MemoryPointers.Logging.NTCrashed,f=__file__,v=__NTversion__)
  NTCrashHandler.handler()
 
