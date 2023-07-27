#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : env_myself.py
@Author     : Gr%1m
@Date       : 18/7/2023 3:56 pm
"""
import sys
from configparser import ConfigParser
from PyQt5.QtGui import QFont

from functions.Mybanner import Banner
from functions.forTools import *
import platform
import os

# 获取项目的绝对路径
ToolsPath = os.path.dirname(os.path.dirname(__file__))
# 编辑默认配置项目
Default_Init = True
Icon_Path = ToolsPath + '/config/tizhongtx.png'

fs_dir = {
    'tab-fs': 16,
    'label-fs': 16,
    'item-fs': 16,
    'button-fs': 14,
    'input-fs': 16,
    'output-fs': 16,
    'default-small': 14,
    'default-big': 16,
}

# --- 配置全局变量 ---

Tools_Exec_List = {}
Gui_WebShell_Func = {}
Gui_PenTools_Func = {}
Gui_VulCheck_Func = {}
Gui_Custom_Func = {}

# - 字体变量
ListWidth = 200
ButtonWidth = 160
ButtonColNum = 5
History_Lines = 1300

InputPlaceholderText = ' [ url ]'
OutputPlaceholderText = f'select a attack type !\n\n\n\n {Banner}'

TabFont = QFont('Dialog', fs_dir['tab-fs'])
LabelFont = QFont('Dialog', fs_dir['label-fs'])
ListItemFont = QFont('Dialog', fs_dir['item-fs'])
ButtonFont = QFont('Dialog', fs_dir['button-fs'])

TextEditFont = QFont('Dialog', fs_dir['input-fs'])
TextBrowserFont = QFont('Dialog', fs_dir['output-fs'])


# ---  定义初始化读取配置函数 --- #
def read_font_config(cff: ConfigParser):
    if cff.has_section('font'):
        fs_dir.update({fs[0]: int(fs[1]) for fs in cff.items('font') if fs[1].isdigit()})
        printl(f"[+] read config.ini get -> {fs_dir}")
    else:
        printl(f"[-] None, failed to read config.ini -> use default setting")


def read_exec_config(cff: ConfigParser):
    if cff.has_section('exec-tools-path'):
        Tools_Exec_List.update({t[0]: t[1] for t in cff.items('exec-tools-path')})

    for name, path in Tools_Exec_List.items():
        Tools_Exec_List[name] = path.split(';;')[0] + os.path.dirname(ToolsPath) + ' '.join(path.split(';;')[1:])


def read_gui(cff: ConfigParser):
    # cff_gui_section = [s for s in cff.sections() if 'dir' in s]

    if cff.has_section('dir-webshell'):
        Gui_WebShell_Func.update({t[0]: t[1] for t in cff.items('dir-webshell')})
        # printl(f"[+] read config get: {Gui_WebShell_Func} ")
    if cff.has_section('dir-pentools'):
        Gui_PenTools_Func.update({t[0]: t[1] for t in cff.items('dir-pentools')})
        # printl(f'[+] read config get: {Gui_PenTools_Func}')
    if cff.has_section('dir-vulcheck'):
        Gui_VulCheck_Func.update({t[0]: t[1] for t in cff.items('dir-vulcheck')})
        # printl(f'[+] read config get: {Gui_VulCheck_Func}')

    # 自由扩展 --> page1 --> button
    # if cff.has_section('dir-xxx*'):
    #     Gui_XXX*_Func.update({t[0]: t[1] for t in cff.items('dir-xxx*')})
    #     printl(f'[+] read config get: {Gui_XXX*_Func}')

    def create_func_link(path=''):
        if path == '':
            return lambda: printl(f'[-] No commands were executed !')

        path = ';;'.join([path.split(';;')[0], os.path.dirname(ToolsPath) + path.split(';;')[1]])
        return lambda: custom_gui_click(path)

    for dirs in [Gui_WebShell_Func, Gui_PenTools_Func, Gui_VulCheck_Func]:
        for name, path in dirs.items():
            dirs.update({name: create_func_link(path)})


# --- main执行初始化操作 --- #
# 创建读取ini文件对象

try:
    cff = ConfigParser()

    if not os.path.exists(f'{ToolsPath}/config.ini'):
        cff.read(f"{ToolsPath}/config.ini")

    elif os.path.exists(f'{ToolsPath}/config/default.ini'):
        cff.read(f"{ToolsPath}/config/default.ini")

    elif platform.system() == 'Linux':
        from functions.forLinux import *

        install()
    elif platform.system() == 'Windows':
        from functions.forWin10 import *

        install()
    else:
        raise ImportError
except ImportError:
    printl("[-] import Tools Failed")
    sys.exit()

except OSError:
    printl(f'[-] OSError')
    sys.exit()
else:
    # 读取文件中的配置
    read_gui(cff)
    read_exec_config(cff)
    read_font_config(cff)
