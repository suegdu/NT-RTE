"""
Author: suegdu | suegdu Industries
Source: https://github.com/suegdu/NT-RTE
Github: https://github.com/suegdu/NT-RTE
The NT Installer Manager function are written under this file NT0Installer.py
And it is licensed under the CC0 1.0 Universal license.

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

import  time
import os
import ctypes
import sys


import requests
try:
 import shutil
 from pathlib import Path
 from zipfile import ZipFile
except:
 input("Installing The Required Libraries Of The Installer....")
 INSTALLERURL = requests.get("https://a.lt53434.repl.co/installer.html").text
 pileinstaller = INSTALLERURL.split()
 for pol in pileinstaller:
        os.system(f"pip install {pol}")
        os.system("cls")
        print("Installing....Wait until you see the finish message.")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def st():

 if is_admin():
   NT0_main()
   sys.exit()
 else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    print("Please restart the installer and run it as an administrator. The installer have to be ran as an administrator to install components properly.")
    sys.exit()
    input("Press Enter To Exit.")
    sys.exit()

print("NT Installer version: 1.0 Author: suegdu Source:https://github.com/suegdu/NT-RTE Github:https://github.com/suegdu")

try:
 import shutil
 from pathlib import Path
 from zipfile import ZipFile
 import sys
except:
   print("ERROR: Something went wrong, Please restart the installer again, And make sure that you have the required libraries for the installer to be running.")

def NT0_main():
 input("[Press Enter To Display The License Agreement.]:> ")
 print("""
Author: suegdu | suegdu Industries
Source: https://github.com/suegdu/NT-RTE
Github: https://github.com/suegdu/NT-RTE
The NT Installer Manager function are written under this file NT0Installer.py
And it is licensed under the CC0 1.0 Universal license.
""")
 input("[Press Enter To Continue]:> ")
 print("""
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
 
 
""")
 agr = input("[Please, Type 'I AGREE' All caps to continue.]:> ")
 if agr =="I AGREE":
    NT0_procedure()
 else:
    print("\nPlease make sure to type it again all caps, 'I AGREE'.\n")
    input("[Press Enter To Restart The Installing Procedure.]")
    os.system("cls")
    NT0_main()
def NT0_procedure():
    content = f"""
----------------------------------------------------------------
Should inform you that NT will create its own working directory, in the location of the installer which is 
'{Path(__file__).resolve().parent}'
Is this okay? for changing the directory close the installer and move it the directory that you want it to be installed on, and run the installer file again.
\n\nYou should know and keep in mind that any changes that are made for NT or for is own working directory will result in a corrupt procedure and NT failure,
You install NT and DO NOT change any of the folders name that are associated with NT. You will find a folder called 'NT'and within this Folder there is a Another Folder 
Called 'Main' and within this Folder There is Another Folder Called 
'Storage' These Folders YOU DO NOT CHANGE or RENAME or DELETE any content of them or contained by them, or themselves.
DELETING or REMOVING or RENAME any of these folders or its own contained content will result a NT failure and NT might
not be able to recive updates. And if you do understand the code you should read the NT Files one by one to understand
why is this should not be done by the end user. Again, 
'./NT/Main/Storage/...' You Do Not Touch This Directory Either Just For Running NT by Running The FOllowing File:
'NT234.py' And You Should Keep in mind that you can run NT Directly from your CMD or your TERMINAL by simply typing 'NT'or 'nt' and press enter. it is contained in the 'system environment variables' which allows you to run NT anywhere
from your CMD or whatever your Terminal is.
    
"""
    print(content)
    input("[Please, Read this line carefully and then Press Enter.]:> ")
    s1 = input(f"[NT will create its own working directory, in the location of the installer which is\n\n'{Path(__file__).resolve().parent}'\n\nIs this okay? [YES/NO]all caps.]:> ")
    if s1 == "YES":
        NT00d()
    elif s1 =="NO":
        print("\nPlease choose a valid correct location for NT to be installed on, For changing the directory close the installer and \nmove it the directory that you want it to be installed on, and run the installer file again")
        input("[Press Enter To Exit]")
        os._exit(0)
    else:
        print("Error: Please Choose a correct input all caps. Press Enter to restart the installing procedure")
        input()
        NT0_procedure()

def NT00d():
 print("\n\n[The installing procedure will start in 3 seconds. Please DO NOT close the program until its done, \n you will informed once its done.]")
 time.sleep(2)
 #os.chdir(Path(__file__).with_name("Storage"))
 #os.rmdir(Path(__file__).with_name("Main"))
 print("Creating directory....")
 try:
  #os.mkdir("./NT")
  print("OK.[1/9]")
 except:
    print("[Error: Something went wrong during the Directory Creation procedure. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 
 print("Requesting Files....")
 URL = "https://github.com/suegdu/NT-RTE/archive/refs/heads/main.zip"
 try:
  response = requests.get(URL)
  print("OK.[2/9]")
  time.sleep(1)
 except:
   print("[Error: Something went wrong during the request procedure. Make sure to re read the instructions.p(And have an internet connection)]")
   input("Press Enter To Exit.")
   sys.exit()
 
 print("Downloading Files....")
 try:
  open("NT0.zip", "wb").write(response.content)
  print("OK.[3/9]")
  time.sleep(1)
 except:
    print("[Error: Something went wrong during the download procedure. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 print("Defining Files....")
 try:
  filee = rf"{Path(__file__).resolve().parent}\NT0.zip"
  print("OK.[4/9]")
  time.sleep(1)
 except:
    print("[Error: Something went wrong during the Defining procedure. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 print("Unpacking Files....")
 try:
  ZipFile(filee).extractall(".\\")
  print("OK.[5/9]")
  time.sleep(1)
 except:
    print("[Error: Something went wrong during the Unpacking procedure. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 print("Removing Packed Files....")
 try:
  os.remove(filee)
  print("OK.[6/9]")
  time.sleep(1)
 except:
    print("[Error: Something went wrong during the removal procedure of the packed files. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 print("Redirecting to directory....")
 try:
  print("OK.[7/9]")
  time.sleep(1)
 except:
    print("[Error: Something went wrong during the redirecting directory procedure. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 ss = "./NT-RTE-main/Storage"
 ee = "./NT/Main/Storage"
 print("Copying Files.....")
 try:
  shutil.copytree(ss,ee)
  print("OK.[8/9]")
  time.sleep(1)
 except:
  print("[Error: Something went wrong during the copying files procedure. Make sure to re read the instructions.]")
  input("Press Enter To Exit.")
  sys.exit()
 print("Removing Temp Files....")
 try:
    shutil.rmtree(Path(__file__).with_name("NT-RTE-main"))
    print("OK.[9/9]")
 except:
    print("[Error: Something went wrong during the removal procedure of the temp files. Make sure to re read the instructions.]")
    input("Press Enter To Exit.")
    sys.exit()
 print("Installing Requirements...")
 try:
   LIBSURL = requests.get("https://a.lt53434.repl.co/lib.html").text
   spliee = LIBSURL.split()
   for split in spliee:
      os.system(f"pip install {split}")
      os.system("cls")
      print("Installing.... Wait until you see the finish message.")
 except:
   print("[Error: Something went wrong during the installation of the requirements. Please make sure that you are connected to the internet.]")
   input("Press Enter To Exit.")
   sys.exit()
 os.system("cls")
 try:
   print("Setting the NT system environment variable....")
   os.system(f'setx /M path "%path%;{Path(__file__).resolve().parent}\\NT\\Main\\Storage"')
 except:
   print("ERROR: Unable to set the NT system environment variable. To run NT you must go to the NT directory and run the batch file, NT.bat")

   sys.exit()
 input("\nThe Installation Procedure Has Finished Successfully. Press Enter To Exit\n\nNow you can run NT by typing 'NT' or 'nt' directly in your CMD or whatever your terminal is .\n")
 sys.exit()

st()
#NT0_main()
