#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : forTools.py
@Author     : Gr%1m
@Date       : 26/7/2023 11:16 am
"""
import subprocess
import platform
from functions.recordlog import printl

if platform.system() == "Linux":
    java8 = "/usr/local/bin/java8 -jar "
    java9 = "/usr/local/bin/java9 -jar "
    java11 = "/usr/local/bin/java11 -jar "
    java17 = "/usr/bin/java -jar "
elif platform.system() == "Windows":
    java8 = ("C:\\Java_Path\\Java_8\\bin\java -jar ").replace("\\", "\\\\")
    java9 = ("C:\\Java_Path\\Java_9\\bin\java -jar ").replace("\\", "\\\\")
    java11 = ("C:\\Java_Path\\Java_11\\bin\java -jar ").replace("\\", "\\\\")
else:
    # platform.system() == "darwin"
    printl(f"[!] 暂时不支持该系统")


def custom_exec_click(path: str):
    path = path.split(';;')[0]
    proc = subprocess.Popen(f'cd workspace; {path} ', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = proc.communicate()
    if stderr != '' and stderr is not None:
        print("Error Command pushed")
    printl(f"[+] Running \n{stdout}")
    return stdout


def custom_gui_click(config: str, pf='Linux'):
    # Linux Use
    cmd = config.split(';;')[0]
    path = config.split(';;')[1]

    if cmd == 'java8':
        java = java8
    elif cmd == 'java11':
        java = java11
    elif cmd == 'java17':
        java = java17
    else:
        java = ''

    proc = subprocess.Popen(f'cd workspace; {java + path} ', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = proc.communicate()

    if stderr != '' and stderr is not None:
        # Error: Unable to access jarfile xxx.jar
        print(f"Error :{stderr}")
    printl(f'[+] New process is running ... \n{stdout}')
    return stdout
