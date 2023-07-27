#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@Author     : Gr%1m
@Date       : 2023-07-15 14:30:33
"""

from PyQt5.QtWidgets import QMainWindow, QTabWidget, QAction, QMessageBox, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from layout.pages import Page1, Page2
from config.env import Icon_Path, TabFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.icon = QIcon(Icon_Path)
        self.tabWidget = QTabWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gr%1m工具箱(专为Linux开发)")
        self.setWindowIcon(self.icon)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        # 初始化页面大小
        self.resize(1200, 700)
        self.setMinimumSize(1050, 360)
        self.setMaximumSize(1920, 1440)

        # 初始化菜单栏
        self.initMenu()
        # 初始化页面
        self.setCentralWidget(self.tabWidget)

        # 创建页面1 2
        self.tabWidget.addTab(Page1(), "GUI TOOLS")
        self.tabWidget.addTab(Page2(), "Command Exec")
        self.tabWidget.setFont(TabFont)

    def initMenu(self):
        exit_act = QAction(QIcon('exit.png'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(qApp.quit)

        reset_act = QAction(QIcon(), '&Reset', self)
        reset_act.triggered.connect(self.reset)

        about_act = QAction(QIcon(), '&about', self)
        about_act.triggered.connect(self.about_me)

        # 初始化菜单栏
        file_menu = self.menuBar().addMenu('&File')
        about_menu = self.menuBar().addMenu('&About')

        file_menu.addAction(reset_act)
        file_menu.addAction(exit_act)
        about_menu.addAction(about_act)

    def reset(self):
        QMessageBox.information(self, "Reset", "This program will reset")

    def about_me(self):
        QMessageBox.information(self, "About Me", f"Power By Gr%1m")


class InitWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具初始化")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)

        # 初始化页面大小
        self.resize(1200, 700)
        self.setMinimumSize(1050, 360)
        self.setMaximumSize(1920, 1440)
