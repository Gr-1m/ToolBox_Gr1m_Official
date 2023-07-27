#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : p2part.py
@Author     : Gr%1m
@Date       : 19/7/2023 5:14 pm
"""
import subprocess

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QTextBrowser, QListWidgetItem
from PyQt5.QtWidgets import QFrame, QPlainTextEdit
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import pyqtSignal, QProcess
from ansi2html import Ansi2HTMLConverter

from layout.p1part import ExecButton
from config.env import ListWidth, InputPlaceholderText, OutputPlaceholderText, History_Lines
from config.env import TextEditFont, TextBrowserFont, ListItemFont


class LeftListLayout(QVBoxLayout):
    item_signal = pyqtSignal(QListWidgetItem)

    def __init__(self, tool_list):
        super().__init__()

        self.tlist = QListWidget()
        self.initList(tool_list)

    def initList(self, tool_list: dict):
        # 创建列表部件,设置列表参数
        self.tlist.setFont(ListItemFont)

        # TODO: name  rename
        for name, path in tool_list.items():
            self.tlist.addItem(CMDItem(name, path))

        self.tlist.itemClicked.connect(self.clicked)
        # 设置按钮的大小策略高度填满，同时指定固定宽度
        self.tlist.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.tlist.setFixedWidth(ListWidth)  # 按钮的固定宽度
        self.addWidget(self.tlist)

    def clicked(self, item):
        self.item_signal.emit(item)


class RightIOLayout(QVBoxLayout):
    # 定义两个信号，分别传递left中选中的项目和输出框对象
    exploit_signal = pyqtSignal(QLineEdit, QTextBrowser)
    help_signal = pyqtSignal(QTextBrowser)

    def __init__(self):
        super().__init__()

        self.input_line = QLineEdit()
        self.output_text = OutputTextBrowser()
        # self.xterm_frame = XtermFrame()
        self.initLayout()

    def initLayout(self):
        # 创建文本输入框 创建文本输出框 # 创建按钮部件
        self.input_line.setFont(TextEditFont)
        self.input_line.setPlaceholderText(InputPlaceholderText)

        self.output_text.setFont(TextBrowserFont)
        self.output_text.setPlaceholderText(OutputPlaceholderText)

        button_area = QHBoxLayout()
        # button_area.heightForWidth(2)

        button1 = ExecButton("Exploit", self.exp_click)
        button2 = ExecButton("Help Clear!", self.help_click)
        button3 = ExecButton("Open Term", self.open_xterm)

        button_area.addWidget(button1)
        button_area.addWidget(button2)
        button_area.addWidget(button3)

        self.addWidget(self.input_line)
        self.addWidget(self.output_text)
        self.addLayout(button_area)

    # 连接按钮点击事件
    def exp_click(self):
        # 发射自定义信号 传递输入框内容和输出框对象
        self.exploit_signal.emit(self.input_line, self.output_text)

    def help_click(self):
        # 发射自定义信号 传递输出框对象
        self.help_signal.emit(self.output_text)

    def open_xterm(self):
        # 发射自定义信号
        subprocess.Popen(f'exo-open --launch TerminalEmulator', shell=True)


class CMDItem(QListWidgetItem):
    def __init__(self, name: str, path: str):
        super().__init__()

        self.setText(name)
        self.setFont(ListItemFont)
        self.setData(100, path)


class OutputTextBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()
        self.converter = Ansi2HTMLConverter()

    def appendText(self, text: str) -> None:
        # 获取当前文本内容的行数
        cursor = self.textCursor()
        html_text = self.converter.convert(text)
        line_count = self.document().blockCount()

        # 如果行数大于10000，则删除第一行文本
        while line_count > History_Lines:
            line_count = self.document().blockCount()
            cursor.movePosition(cursor.Start)
            cursor.movePosition(cursor.NextBlock, cursor.KeepAnchor)
            cursor.removeSelectedText()

        cursor.movePosition(cursor.End)

        self.append(html_text)
        self.setTextCursor(cursor)


class XtermFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.process = None
        self.terminal = QPlainTextEdit()

        self.initFrame()

    def initFrame(self):
        self.terminal.setReadOnly(True)

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.on_ready_read_standard_output)
        self.process.start("xterm")

    def on_ready_read_standard_output(self):
        # 从 QProcess 中读取终端输出并显示在文本框中
        data = self.process.readAllStandardOutput().data()
        output = data.decode("utf-8")
        self.terminal.appendPlainText(output)
