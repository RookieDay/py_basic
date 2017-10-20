#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 18:51
# @Author  : RookieDay
# @Site    : 
# @File    : test1.py
# @Software: PyCharm Community Edition

import numpy as np

list = [[1,2,3,4],[4,1,3,5]]
arr1 = np.array(list)
print(arr1)

# 转换数据格式时，可以用astype函数
arr2 = arr1.astype('str')
print(arr2)
print(arr1 * 4)