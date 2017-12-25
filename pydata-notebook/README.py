#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition


# iloc是通过所在行的数字为索引，loc是所在行的标签为索引，简单讲，iloc是第几行，loc是标签。
# 当索引没有标签时，loc和iloc等价。两者支持冒号的范围选择。

# ix，则是两者的混合，即可以行号，也可以行索引
# df.ix['a','age'] 选择a行 ,列名为age的数值

# ix[ 行1:行2, 列1:列2 ]，iloc和loc也支持行列同时选择