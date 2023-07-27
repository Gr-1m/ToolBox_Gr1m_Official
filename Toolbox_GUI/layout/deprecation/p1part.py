#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : p1part.py.py
@Author     : Gr%1m
@Date       : 26/7/2023 8:55 am
"""
from PyQt5.QtWidgets import *
from functions.forLinux import *
from layout.p1part import ExecButton


class GroupWebShell(QGroupBox):
    def __init__(self):
        super().__init__()

        self.setTitle("WebShell 管理工具  --- ")
        self.initGroup()

    def initGroup(self):
        floor = QVBoxLayout(self)
        row1buttons = QHBoxLayout()
        # row2buttons = QHBoxLayout()

        # row1buttons.setAlignment(Qt.AlignTop)
        row1buttons.setContentsMargins(20, 0, 10, 0)

        for name, path in Gui_WebShell_Func.items():
            button = ExecButton(name, path)
            row1buttons.addWidget(button)

        floor.addLayout(row1buttons)
        self.setLayout(floor)


class GroupBurp(QGroupBox):
    def __init__(self):
        super().__init__()

        self.setTitle("---  渗透利器  --- ")
        self.initGroup()

    def initGroup(self):
        floor = QVBoxLayout(self)
        row1button = QHBoxLayout()

        for name, path in Gui_VulCheck_Func.items():
            button = ExecButton(name, path)
            row1button.addWidget(button)

        floor.addLayout(row1button)
        self.setLayout(floor)


class GroupXxx(QGroupBox):
    def __init__(self):
        super().__init__()

        self.setTitle("---  x x x x  --- ")
        self.initGroup()

    def initGroup(self):
        floor = QVBoxLayout(self)
        row1button = QHBoxLayout()

        for name, path in Gui_PenTools_Func.items():
            button = ExecButton(name, path)
            row1button.addWidget(button)

        floor.addLayout(row1button)
        self.setLayout(floor)
