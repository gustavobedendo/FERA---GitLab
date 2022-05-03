# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:54:39 2022

@author: labinfo
"""
import os, platform, re, hashlib, sys, mmAssembler
plt = platform.system()

def get_application_path():
    application_path = None
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    elif __file__:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path

def md5(path_pdf):
    hash_md5 = hashlib.md5()
    with open(path_pdf, "rb") as f:
        cont = 0
        #if(os.path.getsize(path_pdf)>4096 * 1024 * 8 + 1):
        #    f.seek(- 4096 * 1024 * 8, 2)
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    digest = hash_md5.hexdigest()
    print(path_pdf, digest)
    return digest

def check_version(): 
    regex = r"FERA ([0-9]+)\.([0-9]+)\-([0-9]+)"
    pattern = re.compile(regex)
    if plt == "Linux":
        None
    elif plt=="Windows":        
        try:
            folder = r"\\Desktop-vqtcb8s\mmassembler_control_version"
            file_version = os.path.join(folder, "mmassembler_version.txt")
            version = None
            release = None
            date = None
            
            with open(file_version) as file:
                lines = file.readlines()
                for line in lines:
                    #if("version=" in line):
                    #    version = int(line.split("version=")[1])
                    #if("release=" in line):
                    #    release = int(line.split("release=")[1])
                    #if("date=" in line):
                        date = int(line.split("date=")[1])
            if(date == None): #or version == None or release == None):
                return -1
            else:
                if(version==int(global_settings.version)):
                    if(int(global_settings.release) < release):
                        return 0
                    elif(int(global_settings.release) == release):
                        return 1
                    else:
                        return -1
                else:
                    return -1
        except:
            return -1
                