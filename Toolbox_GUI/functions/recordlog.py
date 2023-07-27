#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : recordlog.py
@Author     : Gr%1m
@Date       : 19/7/2023 8:36 am
"""

import time


def printl(context, record_log=True, end='\n') -> str:
    try:
        if context[0] == '[' and context[2] == ']':
            prompt = context[1].lower()
            main_text = context[3:].lstrip()
            if prompt.lower() == 'i':
                context = '\x1b[01;30;30m[i]\x1b[0m ' + main_text
            elif prompt == '-':
                context = '\x1b[01;30;31m[-]\x1b[0m ' + main_text
            elif prompt == '0':
                context = '\x1b[01;30;32m[0]\x1b[0m ' + main_text
            elif prompt.lower() == 'w':
                context = '\x1b[01;30;33m[W]\x1b[0m ' + main_text
            elif prompt == '+':
                context = '\x1b[01;30;34m[+]\x1b[0m ' + main_text
            elif prompt == '*':
                context = '\x1b[01;30;35m[*]\x1b[0m ' + main_text
            elif prompt.upper() == 'F':
                context = '\x1b[01;30;36m[F]\x1b[0m ' + main_text
            else:
                context = '\x1b[01;30;37m[!]\x1b[0m ' + main_text
            del prompt, main_text
        else:
            context = '\x1b[01;30;38m[?]\x1b[0m ' + context.lstrip()
    except IndexError:
        context = '\x1b[01;30;37m[E]\x1b[0m ' + f"Log Input Error:{context.lstrip()}"

    finally:
        context = f"[\x1b[01;30;32m{time.asctime().split()[3]}\x1b[0m] {context}"
        if record_log:
            print(context, end=end)
        return context
