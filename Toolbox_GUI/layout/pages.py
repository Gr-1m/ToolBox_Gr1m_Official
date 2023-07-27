#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@Author     : Gr%1m
@Date       : 2023-07-15 14:30:33
"""
import time
import subprocess

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QListWidgetItem, QLineEdit

from layout.p1part import GroupX
from layout.p2part import LeftListLayout, RightIOLayout, OutputTextBrowser
from config.env import Gui_WebShell_Func, Gui_PenTools_Func, Gui_VulCheck_Func, Tools_Exec_List, printl


class Page1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_page()

    def init_page(self):
        page_floor = QVBoxLayout(self)

        g_webshell = GroupX("---  WebShell 管理工具  --- ", Gui_WebShell_Func)
        g_pentools = GroupX("---  渗透利器  --- ", Gui_PenTools_Func)
        g_vulcheck = GroupX("---  漏洞检查  --- ", Gui_VulCheck_Func)

        page_floor.addWidget(g_webshell, 2)
        page_floor.addWidget(g_pentools, 3)
        page_floor.addWidget(g_vulcheck, 5)

        # 自定义增加按钮区块 --> env 读取 --> read_func
        # g_XXX* = GroupX("--- XXX* ---", Gui_XXX*_Func)
        # page_floor.addWidget(g_XXX*, 2)


class Page2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.select_item = QListWidgetItem()
        self.select_current_item = None
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)

        # 创建两侧垂直布局
        left_layout = LeftListLayout(Tools_Exec_List)
        right_layout = RightIOLayout()

        # 接收左右侧框架传递信号
        left_layout.item_signal.connect(self.get_item)
        right_layout.exploit_signal.connect(self.run_exploit)
        right_layout.help_signal.connect(self.return_help)
        # 渲染左右侧框架
        # 将左右侧布局添加到主布局
        layout.addLayout(left_layout, 25)
        layout.addLayout(right_layout, 75)

        self.setLayout(layout)

    # 下面三个函数是按钮需要的参数，以及两个按钮触发的操作
    def get_item(self, item: QListWidgetItem):
        self.select_current_item = item
        printl(f"[+] Page2.select_current_item -> {item.data(100)}")

    def run_exploit(self, input_line: QLineEdit, output: OutputTextBrowser):
        # from PyQt5.QtWidgets import QMessageBox
        # QMessageBox.information(self, "Confirm", f"You should confirm The Action !")
        output.clear()
        output.appendText(f"{self.select_current_item.data(100)} is Running")
        if self.select_current_item != self.select_item:
            # 判断所选项目是否有改变，在执行操作后刷新文本浏览器
            self.select_item = self.select_current_item
            output.clear()
            output.reload()

        if self.select_current_item is None:
            output.append(f"No Command Input")
        elif input_line is None:
            output.append(f"No Target URL !")
        else:
            proc = subprocess.Popen(f"{self.select_current_item.data(100)} {input_line.text()}",
                                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            wait_time, start_time = 0, 0

            while True:  # 实时将命令执行情况展示到输出框
                result = proc.stdout.readline().decode()
                if result == '' and proc.poll() is not None:
                    break
                elif result == '' and proc.poll() is None:
                    if wait_time == 0:
                        start_time = time.time()
                        wait_time += 1
                        time.sleep(10)
                    else:
                        if time.time() - start_time > 10:
                            break
                        else:
                            time.sleep(10)
                else:
                    start_time = time.time()
                    output.appendText(result.rstrip())

    def return_help(self, output: OutputTextBrowser):
        output.clear()
        output.reload()

        if self.select_current_item is None:
            output.append("No Command Selected")
        else:
            cmd = self.select_current_item.data(100)
            proc = subprocess.Popen(f"{cmd.split(' ')[0]} --help",
                                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while True:
                result = proc.stdout.readline().decode()
                if result == '' and proc.poll() is not None:
                    break
                else:
                    output.appendText(result.rstrip())

        output.reload()
