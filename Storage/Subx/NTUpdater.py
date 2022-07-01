import os
import shutil
import requests
from pathlib import Path
from zipfile import ZipFile
import sys
import time
from swinlnk.swinlnk import SWinLnk
input("[Press Enter to start the update procedure]:> ")
print("The update procedure will start in 4 seconds, Please do not close the program or the update procedure will be corrupted.\nYou will be informed once its done.")
time.sleep(4)
#os.chdir(Path(__file__).with_name("Storage"))
#os.rmdir(Path(__file__).with_name("Main"))
print("Updating directory....")
try:
 shutil.rmtree(Path(__file__).with_name("Main"))
 print("OK.[1/9]")
 time.sleep(1)
except:
   print("[Error: Something went wrong during the removal procedure of the old directory. Make sure to re read the instructions.]")
   input("Press Enter To Exit.")
   sys.exit()

print("Requesting Files....")
URL = "https://github.com/suegdu/NT-RTE/archive/refs/heads/main.zip"
try:
 response = requests.get(URL)
 print("OK.[2/9]")
 time.sleep(1)
except:
  print("[Error: Something went wrong during the request procedure. Make sure to re read the instructions.]")
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
ss = "./NT-RTE-main"
ee = "./Main"
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
   input("Enter To Exit")
   sys.exit()
try:
    print("Finals.....")
    swl = SWinLnk()
    swl.create_lnk(f'{Path(__file__).resolve().parent}\\NT\\Main\\Storage\\NT234.py', f'{Path(__file__).resolve().parent}\\NT\\Main\\Storage\\NT.lnk')
except:
    print("[Error: Something went wrong during the finals procedure. Make sure to re read the instructions.]")
    input("Enter To Exit")
    sys.exit()
input("The Installation Procedure Has Finished Successfully. Press Enter To Exit")
sys.exit()
