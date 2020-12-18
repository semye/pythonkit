#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 用来指定字符集 默认为ASCII码

import os

filePath = os.path.realpath(__file__)
dirPath = os.path.dirname(filePath)
print(dirPath)
fileList = os.listdir(dirPath)

for fileItem in fileList:
    print(fileItem.title().lower())
    if fileItem.endswith('.json'):
        os.rename(fileItem, "../resources/rename1.json")
