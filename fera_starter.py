# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:09:19 2022

@author: labinfo
"""

import subprocess

def get_application_path():
    application_path = None
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    elif __file__:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path

if __name__ == '__main__':  
    try:  
        None
    except:
        None