# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 15:54:39 2022

@author: labinfo
"""
import os, platform, re, hashlib, sys
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

if __name__ == '__main__':   
    regex = r"FERA ([0-9]+)\.([0-9]+)\-([0-9]+)"
    pattern = re.compile(regex)
    if plt == "Linux":
        None
    elif plt=="Windows":        
        folder = r"\\192.168.10.9\tecnicos\Instaladores\FERA - Forensics Evidence Report Analyzer"
        for file in os.listdir(folder): 
            file_abs_path = os.path.join(folder, file)
            if(os.path.isdir(file_abs_path)):
                if(pattern.match(file)):
                    b_version, l_version, date = pattern.findall(file)[0]
                    print(b_version, l_version, date)
