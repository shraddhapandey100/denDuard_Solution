
'''DenGuard Antivirus Engine  Script .'''
#import the library


import hashlib
from importlib.resources import path
from posixpath import dirname
from sys import maxsize
import os
from tkinter import UNDERLINE
########################


# Global Variable

malware_hashes= list(open("virusHash.denvit", "r").read().split('\n'))
virusInfo= list(open("virusInfo.denvit","r").read().split('\n'))


# Get the Hash of the file

def sha256_hash(filename):
    try:
        with open(filename,"rb") as f:
            bytes= f.read()
            sha256_hash= hashlib.sha256(bytes).hexdigest()

            f.close()
        print (sha256_hash)
        return sha256_hash
    except:
        pass 
        return 0

# Malware Detection By Hash


def malware_checker(pathOfFile):
     global malware_hashes
     global virusInfo

     hash_malware_check= sha256_hash(pathOfFile)
     counter= 0


     for i in malware_hashes:
         
         if i== hash_malware_check:
             return virusInfo[counter]
             
         counter+=1
     return 0



# Malware Detection In folder


virusName= []
virusPath= []

def virusScanner(path):
    # Get the list of all files and directories tree at given path
    
    dir_list= list()
    #fileName= ""
    for(dirpath,dirnames,filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath,file)for file in filenames]

    for i in dir_list:
        print(i)
        if malware_checker(i)!=0:
            virusName.append(malware_checker(i)+" :: File :: "+i)
            virusPath.append(i)

# Virus Remover

def virusRemover(path):
    try:
        virusScanner(path)
        if virusPath:
            for i in virusPath:
                os.remove(i)
        else:
            return 0
    except:
        print("There is no more affected file")
    


# Junk File Remover

def junkFileRemover():
    # temp file remover
    temp_list= list()

    # Window username
    username= os.environ.get('USERNAME').upper().split(" ")

    for(dirpath,dirnames,filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath,file)for file in filenames]

    for(dirpath,dirnames,filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(dirpath,file)for file in filenames]
    for(dirpath,dirnames,filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath,file)for file in filenames]

   # print(temp_list)
   
    if temp_list:
            for i in temp_list:
                try:
                    print(i)
                    os.remove(i)
                except:
                    pass
                try:
                    print(i)
                    os.rmdir(i)
                except:
                    pass
    else:
        return 0   

 # RamBooster function


def ramBooster():
    try:

        task_list= ["notepad.exe","AnyDesk.exe","msedge.exe","TeamViewer_Service.exe",
                "tmaster.exe","inkscape.exe","firefox.exe","vlc.exe",
                "chrome.exe","GOM.exe","msedge.exe","POWERPNT.exe","Word.exe","Excel.exe"]
    # task Kill



    
        for i in task_list:
            
            if (i):
                try:
                    os.system("taskkill /f /im {}".format(i))
                except:
                    pass
            else:
                pass
            
    except:
        print("Process is not running in the system.")
        


