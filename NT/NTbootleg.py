from msvcrt import getch
import time
import sys
import os
from pathlib import Path
from zipfile import ZipFile
from colorama import Fore,Style,Back, init
from datetime import datetime
from distutils.dir_util import copy_tree
import shutil
from numba import jit
import random
parent = Path(__file__).with_name("NT")
os.system("title Starting....")
try:
 os.mkdir(Path(__file__).with_name("NT"))
 os.chdir(parent)
except FileExistsError:
    os.chdir(parent)
System234 = """





"""

sysdir = "./NTSysMain"
NTdir = "./NT"
syst = os.path.exists("./NTSysMain/appli298")
def checkingmain():
    if syst==True:
        try:
         os.chdir(sysdir)
         os.startfile("NT234.py")
        except FileNotFoundError:
            print("Error: NT File Not Found")
            logregister("Error: NT File Not Found")
        except:
            print("Error: Something Went Wrong 0-4446")
            logregister("Error: An Unknown Error Hass Been Occurred 0-4446")
    elif syst==False:
        main()
        print(Style.RESET_ALL)
        print("The Installation Has Finished. Press Any Key To Exit")
        logregister("Installation Finished.")
        getch()
        sys.exit()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
componentsfile = Path(__file__).with_name("NTSysMain.zip")
Components_exists = os.path.exists(componentsfile)
print(Components_exists)
init()
__installer__ = "bootleg1.0"
__NT__ = "NT2341.0"
def logregister(str):
    try:
     with open("NTbootleg.log","a+") as NTlogfile:
        NTlogfile.write(f"[{current_time}]: {str}\n")
    except FileNotFoundError:
        create = open("NTbootlet.log", "a")
        create.close()
        return
logregister("bootleg Started")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(00.01)
def main():
 os.system("title NT Installer 1.0")
 logregister("Start.")
 print("""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  NT Installer 1.0
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  The Purpose of this
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  procedure is to install
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  NT and all its files and
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  components. Follow the
&&&&&&&&&&&&&&&&&&&&&&&&&&&@@&&&&&&&&&&@@&&&&@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  described instructions.
&&&&&&&&&&&&&&&&&&&&&&&&&@@@&&&&&&&&&&&@@@@@@@@@@@&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&@@@@&&&&&&@@@@@@@@@&&&&&&&@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@&&&&&&&&&@@@@@&&&&&&&&&&&@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@&&&&&&&@@@@@@@&&&&&&&&&&&&@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&@@&&&&@@@@&&@@@@@@@@@@@@&&&&&&&&&&@@@&@@@@&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&@@@@&&&&&@@@@&&&&&&&@@@@@@@@@@@@@@@@@&&@@@@@&&&&&&&&&&&&&&&&&&&&&  If you contiuned facing
&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@&&&&&@@@@@&&&&&&@@@@@@@@@@@@&&&@@@@&&&&&&&&&&&&&&&&&&&&&&  this screen you should
&&&&&&&&&&&&&&&&&&&&@@&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@@@@&&&&&&&&&&&&&&&&&&&&&  report with a specific
&&&&&&&&&&&&&&&&&&&&@@@@&&&&&&&&&&&@@@@@@@@@@@&&&&&&&&@@@@@@@@@@@@&&@@&&&&&&&&&&&&&&&&&&&&  details. (the log file)
&&&&&&&&&&&&&&&&&&&&&&&@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  Author: suegdu on Github
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  suegdu Industries 2021-2022
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  github.com/suegdu/NT-RTE
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@&&&&@&&&&&@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&@@&&&@&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&@&&@&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&@@@&&&&&&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  """)
 print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
 print("Press Any Key To Continue The Procedures Of The Installation ->")
 logregister("starting the installing process.")
 getch()
 os.system("cls")
 os.system("title Status: Installing NT...")
 print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTYELLOW_EX}INFO{Fore.LIGHTBLACK_EX}]:> Checking Components....")
 logregister("Checking Components.")
 time.sleep(3)
 try:
  if Components_exists==True:
     print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTYELLOW_EX}INFO{Fore.LIGHTBLACK_EX}]:> Done")
     logregister("Components Are exist.")
  elif Components_exists==False:
     os.system("title NT Installer: ERROR")
     print(Fore.LIGHTBLACK_EX+f"[{Fore.RED}ERROR{Fore.LIGHTBLACK_EX}]:> Components files are missing. ({componentsfile}) try to do a fresh re install for the entire NT procedure and make sure to do not delete any files.")
     logregister("ERROR: Components files are missing. try to do a fresh re install for the entire NT procedure and make sure to do not delete any files.")
     print("Press Any Key To Exit.")
     getch()
     sys.exit()

 except:
     os.system("title NT Installer: ERROR")
     print(Fore.LIGHTBLACK_EX+f"[{Fore.RED}ERROR{Fore.LIGHTBLACK_EX}]:> Something Went Wrong While Chekcing Components.")
     logregister("ERROR: Something Went Wrong While Chekcing Components.")
     print("Press Any Key To Exit.")
     getch()
     sys.exit()
 logregister(f"done checking components. {Components_exists}")
 print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTGREEN_EX}UNPACKING{Fore.LIGHTBLACK_EX}]:> UnPacking Components....")
 time.sleep(2)
 logregister("Unpacking Components.")
 try:
  logregister("un zipping Components")
  ZipFile(componentsfile).extractall(Path(__file__).with_name("NT"))
  logregister("done un zipping Components")
  print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTGREEN_EX}UNPACKING{Fore.LIGHTBLACK_EX}]:> Done")
 except:
    logregister("ERROR: Something Went Wrong While Unpacking The Components. ")
    print(Fore.LIGHTBLACK_EX+f"[{Fore.RED}ERROR{Fore.LIGHTBLACK_EX}]:> Something Went Wrong While Unpacking The Components.")
    print("Press Any Key To Exit.")
    getch()
    sys.exit()
 print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTYELLOW_EX}INFO{Fore.LIGHTBLACK_EX}]:> Copying Components....")
 logregister("Started Copying Components.")
 """ try:
     logregister("Started Moving")
     shutil.move(sysdir, NTdir)
     logregister("Done Moving")
     print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTYELLOW_EX}INFO{Fore.LIGHTBLACK_EX}]:> Done")
 except FileNotFoundError:
     logregister("ERROR: The Components File Expetion: FileNotFoundError")
     print(Fore.LIGHTBLACK_EX+f"[{Fore.RED}ERROR{Fore.LIGHTBLACK_EX}]:> The Components File Is Not Exist.")
     print('Press Any Key To Exit.')
     getch()
     sys.exit()
 except:
     logregister("ERROR: Something Went Wrong While Moving The Components Files. ")
     print(Fore.LIGHTBLACK_EX+f"[{Fore.RED}ERROR{Fore.LIGHTBLACK_EX}]:> Something Went Wrong While Moving The Components.")
     print("Press Any Key To Exit.")
     sys.exit()"""


 print(Fore.LIGHTBLACK_EX+f"[{Fore.LIGHTYELLOW_EX}INSTALLING{Fore.LIGHTBLACK_EX}]:> Installing NT....")
 logregister("installing NT")
 time.sleep(2)
 with open("NT234.py", "a") as sysfile:
   logregister("started writing the file....")
   sysfile.write(System234)
 os.chdir("NTSysMain")
 syste = open("appli298","a")

 syste.close()















checkingmain()