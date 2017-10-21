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
print('\t')
print(arr1.shape)   #矩阵尺寸 几行几列
print('\t')
# 转换数据格式时，可以用astype函数
arr2 = arr1.astype('str')
print(arr2)
print(arr1 * 4)

print('***********************')
c = [[1,3],[5,6]]
d = np.array(c)
print(d)
print(d.shape)
print(d.size)
print(d.max(axis=0))          	# 找维度0，也就是最后一个维度上的最大值，array([3, 4])
print(d.max(axis=1))          	# 找维度1，也就是倒数第二个维度上的最大值，array([2, 4])
print(d.mean(axis=0))          	# 找维度0，也就是第一个维度上的均值，array([ 2.,  3.])
print(d.flatten())             	# 展开一个numpy数组为1维数组，array([1, 2, 3, 4])
print(np.ravel(c))             # 展开一个可以解析的结构为1维数组，array([1, 2, 3, 4])
