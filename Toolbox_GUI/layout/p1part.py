#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@project    : Toolbox_GUI
@file       : p1part.py
@Author     : Gr%1m
@Date       : 19/7/2023 5:00 pm
"""
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt

from config.env import ButtonFont, ButtonWidth, ButtonColNum


class GroupX(QGroupBox):
    def __init__(self, title, path_dir):
        super().__init__()

        self.setTitle(title)
        self.initGroup(path_dir)

    def initGroup(self, path_dir: dict):
        floor = QVBoxLayout(self)
        rows_button = []
        for i in range(len(path_dir) // ButtonColNum + 1):
            rows_button.append(QHBoxLayout())
            rows_button[i].setAlignment(Qt.AlignLeft)

        count = 0
        for name, path in path_dir.items():
            button = ExecButton(name, path)
            rows_button[count // ButtonColNum].addWidget(button)
            count += 1

        for row in rows_button:
            floor.addLayout(row)

        del rows_button, count
        self.setLayout(floor)


class ExecButton(QPushButton):
    def __init__(self, name, operate):
        super().__init__()

        self.setText(name)
        self.initProp()
        self.clicked.connect(operate)

    def initProp(self):
        self.setFont(ButtonFont)
        # 设置按钮的大小策略为固定大小，同时指定固定宽度
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedWidth(ButtonWidth)  # 按钮的固定宽度
