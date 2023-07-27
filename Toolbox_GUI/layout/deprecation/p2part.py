#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : p2part.py
@Author     : Gr%1m
@Date       : 26/7/2023 8:58 am
"""
from PyQt5.QtWidgets import *


class OutputTextBrowser(QTextBrowser):
    def __init__(self):
        super().__init__()

    def appendText_old(self, text: str) -> None:
        # 获取当前文本内容
        cursor = self.textCursor()
        current_text = self.toPlainText()

        # 将文本内容按行分割成列表
        lines = current_text.split('\n')

        # 如果行数大于10000，则删除第一行文本
        while len(lines) > 100:
            lines.pop(0)

        # 更新文本浏览器的内容
        self.setPlainText('\n'.join(lines))

        cursor.movePosition(cursor.End)
        self.setTextCursor(cursor)
        self.append(text)
