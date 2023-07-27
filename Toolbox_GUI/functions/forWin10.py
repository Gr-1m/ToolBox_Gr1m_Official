#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : forWin10.py
@Author     : Gr%1m
@Date       : 18/7/2023 3:53 pm
"""
import sys

from functions.forTools import *


def install():
    proj_dir = os.path.dirname(ToolsPath)
    tool_dirs = ['webshell', 'pentools', 'vulcheck', 'execlist']

    for tdir in tool_dirs:
        if os.path.exists(f'{proj_dir}\\{tdir}'):
            printl(f'[*] {proj_dir}\\{tdir} is exists')
        else:
            os.mkdir(f'{proj_dir}\\{tdir}')
            printl(f'[+] {proj_dir}\\{tdir} make success')

    printl(f'[*] please run The "install.bat" as Administator')
    sys.exit()


# WebShell管理工具
def godzilla_click(self, event):
    subprocess.Popen(f"cd gui_webshell/Godzilla && {java8} -jar Godzilla.jar", shell=True)


def behinder_click(self, event):
    subprocess.Popen(f"cd gui_webshell/Behinder && {java8} -jar Behinder.jar", shell=True)


def BehinderMode_click(self, event):
    subprocess.Popen(f"cd gui_webshell/Behinder-Mode && {java8} -jar Behinder-Mode.jar", shell=True)


def antSword_click(self, event):
    subprocess.Popen(f'cd gui_webshell/AntSword/AntSword-Loader-v4.0.3-win32-x64 && AntSword.exe', shell=True)


def tianxie_click(self, event):
    subprocess.Popen(f"cd gui_webshell/TianXie && {java8} -jar 天蝎权限管理工具.jar", shell=True)


Gui_WebShell_Func = {}
Gui_PenTools_Func = {}
Gui_VulCheck_Func = {}
Gui_Custom_Func = {}
