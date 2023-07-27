#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : tray.py
@Author     : Gr%1m
@Date       : 25/7/2023 4:03 pm
"""
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu, qApp
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon

from config.env import *


class Tray(QObject):
    tray_click = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.trayi = QSystemTrayIcon(self)
        self.trayi.setIcon(QIcon(Icon_Path))
        self.traymenu = QMenu()
        self.a1 = QAction('&重置', )
        self.a2 = QAction('&退出', )
        self.initTray()

    def initTray(self):
        self.a1.triggered.connect(lambda: 0)
        self.a2.triggered.connect(qApp.exit)

        self.traymenu.addAction(self.a1)
        self.traymenu.addAction(self.a2)

        self.trayi.setContextMenu(self.traymenu)
        self.trayi.activated.connect(self.act)
        self.trayi.show()  # 不调用show不会显示系统托盘

    def act(self, reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            self.tray_click.emit("main_show")
