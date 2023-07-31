#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@Author     : Gr%1m
@Date       : 2023-07-15 14:30:33
"""
import sys
from PyQt5.QtWidgets import QApplication

from functions.recordlog import printl
from layout.baseboard import MainWindow
from layout.tray import Tray


class MyApp:
    def __init__(self):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)  # 最小化托盘用,关闭所有窗口也不结束程序
        self.mainwindow = MainWindow()
        self.tray = Tray()
        self.initMyUI()

    def initMyUI(self):
        # app_init()
        printl("[+] ---- 初始化成功 ---- ")
        self.tray.tray_click.connect(self.show_window)

    def run(self):
        try:
            self.mainwindow.show()
            sys.exit(self.app.exec_())
        except KeyboardInterrupt:
            printl("[-] **** 程序异常退出 ****")

    def show_window(self):
        self.mainwindow.show()


def app_init():
    import os
    if os.path.exists('config.ini'):
        printl(f'[+] Find config.ini')
        ConfigFile = 'config.ini'
    else:
        printl(f'[-] No config.ini')
        printl(f'[+] Write DEFAULT into config.ini ')
        ConfigFile = 'config/defaults'


def test_start():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # 最小化托盘用,关闭所有窗口也不结束程序
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start = MyApp()
    start.run()
