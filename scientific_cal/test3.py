#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/21 22:49
# @Author  : RookieDay
# @Site    : 
# @File    : test3.py
# @Software: PyCharm Community Edition

import pandas as pd

data1 = [['分析师','数据分析','数据挖掘','数据'],['数据', '顾问', '销售', '分析师']]

s1 = pd.Series(data1,index=['a','b'])
print(s1)
