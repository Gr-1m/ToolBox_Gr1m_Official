# 专为Linux开发的安全工具箱  -- v0.8

工具箱版本: 

    个人专属版本
    正式版v1.0
    内测版v0.8 - v0.9


baseboard.py: 图形化界面的底板 
pages.py: 页面主体创建
page1-3.py: 各个页面的类
tray.py: 系统托盘类

## 使用说明
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r reqirements.txt
python3 GUImain.py 
```

## 功能简介
第一页: 
一些内置的图形化工具，也可以自定义的按钮

第二页: 
一些命令执行类工具，可以在本程序内运行，目前版本推荐点击下面按钮打开终端运行

末页:
提供一些编码解码，加解密算法的使用（目前在开发中）

## 使用前必读！！！

首次运行请执行安装：`sudo chmod +x ./install.sh && sudo ./install.sh`（暂时未完善安装脚本，请自行安装相关工具）

> 初始化config.ini， 当该文件读取不到，不存在时程序读取默认配置config/default.ini。

config.ini 中的工具配置为：
`toolname = [command];;[path];;[option]`


### 参考来自 & 鸣谢：

[one-fox](https://mp.weixin.qq.com/s/NiW-5LpvTqVlkL8tuUV6HQ)工具箱 by 狐狸师傅



感谢 [JetBrains](https://www.jetbrains.com/) 提供的一系列好用的 IDE 和对本项目的支持。

![JetBrains Logo (Main) logo](https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.svg)



