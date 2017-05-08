# -*- coding: utf-8 -*-
# 遍历当前文件夹目录
import os

L = [d for d in os.listdir('.')] # 打出当前文件夹的目录
print(L)