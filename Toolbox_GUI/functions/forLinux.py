#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : forLinux.py
@Author     : Gr%1m
@Date       : 18/7/2023 3:52 pm
@Comment    : Linux部分暂时只支持Debian系列，包管理器为apt的版本
"""
import os, sys
from functions.forTools import *

java8 = "/usr/local/bin/java8 -jar "
java9 = "/usr/local/bin/java9 -jar "
java11 = "/usr/local/bin/java11 -jar "
java17 = "/usr/bin/java -jar "

ToolsPath = os.path.dirname(os.path.dirname(__file__))


def install():
    proj_dir = os.path.dirname(ToolsPath)
    tool_dirs = ['webshell', 'pentools', 'vulcheck', 'execlist']

    for tdir in tool_dirs:
        if os.path.exists(f'{proj_dir}/{tdir}'):
            printl(f'[*] {proj_dir}/{tdir} is exists')
        else:
            os.mkdir(f'{proj_dir}/{tdir}')
            printl(f'[+] {proj_dir}/{tdir} make success')

    printl(f'[*] please run The "install.sh" as root privileges')
    sys.exit()


# WebShell管理工具
def godzilla_click():
    subprocess.Popen(f"cd /opt/PenTools/webshell/Godzilla && {java8} -jar godzilla.jar", shell=True)


def behinder4_click():
    subprocess.Popen(f"{java8} -jar /opt/PenTools/webshell/Behinder/Behinder.jar", shell=True)


def BehinderMode_click():
    subprocess.Popen(f"", shell=True)


def tianxie_click():
    subprocess.Popen(f"{java8} -jar /opt/PenTools/webshell/TianXie/天蝎权限管理工具.jar", shell=True)


def antSword_click():
    subprocess.Popen(f'/opt/PenTools/webshell/AntSword-Loader-v4.0.3-linux-x64/AntSword', shell=True)


def burpsuite_click():
    subprocess.Popen(f'/usr/local/opt/burpsuit_pro/burpsuit_pro.sh', shell=True)


def dogcs_click():
    subprocess.Popen(
        f'{java11} -jar /opt/PenTools/WinTools/ONE-FOX集成工具箱_V2.0魔改版_by狐狸/gui_other/dogcs_v2.1/dogcs.jar')


def yakit_click():
    subprocess.Popen(f'/opt/AppMenu/Yakit-1.2.2-linux-amd64.AppImage', shell=True)


def apttools_click():
    subprocess.Popen(f'/usr/pentools/bin/apt-tools', shell=True)


def thinkphpexp_click():
    subprocess.Popen(f'/usr/pentools/bin/ThinkPHPexp', shell=True)


def springboot_click():
    subprocess.Popen(f'/usr/pentools/bin/SpringBootExp', shell=True)


def weblogic_click():
    subprocess.Popen(f'/usr/pentools/bin/weblogicTools', shell=True)


def shiroattack_click():
    subprocess.Popen(f'/usr/pentools/bin/shiroAttack', shell=True)


Tools_Exec_List = {
    'afrog': '/usr/pentools/bin/afrog -t ',
    'dalfox': '/usr/pentools/bin/dalfox url ',
    'FastJsonScan': '/usr/pentools/bin/fastjsonScan -u ',
    'fscan': '/usr/pentools/bin/fscan -u ',
    'Pwn-Xss': '/usr/pentools/bin/pwnxss -u ',
    'Struct2Scan': '/usr/pentools/bin/Struct2Scan -u ',
    'xray': '/usr/pentools/bin/xray',
}

Gui_WebShell_Func = {
    'AntSword': antSword_click,
    'Behinder': behinder4_click,
    'Godzilla': godzilla_click,
    'TianXie': tianxie_click,
}

Gui_PenTools_Func = {
    'Burpsuite_pro': burpsuite_click,
    'CobaltStrike_4.7': lambda: custom_exec_click(f'/usr/bin/whoami'),
    'dogcs_v2.0.1': lambda: custom_gui_click(
        f'java11;;/opt/PenTools/WinTools/ONE-FOX集成工具箱_V2.0魔改版_by狐狸/gui_other/dogcs_v2.1/dogcs.jar'),
    'Yakit-1.2.2': yakit_click,
    'goby-v2.5': lambda: custom_exec_click(f'/opt/goby-linux-x64-2.6.0/goby'),
    'apt-tools': apttools_click,
}
Gui_VulCheck_Func = {
    'ThinkPHP': thinkphpexp_click,
    'SpringBoot': springboot_click,
    'WebLogicTool': weblogic_click,
    'ShiroAttack': shiroattack_click,
}

Gui_Custom_Func = {
    'test1': custom_exec_click,
    'test2': lambda: print(1),
    'test3': lambda: print(1),
}
