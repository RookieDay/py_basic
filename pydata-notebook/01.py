#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25
# @Author  : RookieDay
# @Site    : 
# @File    : 01
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition


import numpy as np
import pandas as pd
df1 = pd.DataFrame(np.arange(4).reshape(2,2),columns = ['a','b'])
df2 = pd.DataFrame(np.arange(6).reshape(2,3),columns = ['a','b','c'])
print(df1)
# print('*'*40)
# print(df1.iloc[1])
# print('*'*40)
# print(df1.loc[1])
print('*'*40)
print(df1.ix[0,'b'])