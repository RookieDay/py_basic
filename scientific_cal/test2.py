#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/20 20:28
# @Author  : RookieDay
# @Site    : 
# @File    : test2.py
# @Software: PyCharm Community Edition
import pandas as pd
import numpy as np

s = pd.Series([1,2,3],index=['a','b','c'])
print(s)
print(s.index)
print(s['a'])
print('------------------------')
d = {'sex':'male','age':12}
s2 = pd.Series(d,index=['sex','age','mm'])
print(s2)
print(s2['age'])

print('****************************')
ditc = {
    'name':['zhansan','ana','bob'],
    'sex':['male','zhong','female'],
    'age':[11,12,32]
}
df = pd.DataFrame(ditc)
print(df)
print('&&&')
print(df.info())
print('---')
print(df.age.astype('str'))
print('\t')
print(df['name'])
print(df.name)
print(df.ix[0])
print(df.index)
print(df[['age','sex']])

print('\t')
print(df[df.age>22])

print('\t')
print(df.sex == 'male')

print('\t')
dfs1 = pd.DataFrame(np.arange(4).reshape(2,2),columns=['a','b'])
dfs2 = pd.DataFrame(np.arange(6).reshape(2,3),columns=['a','b','c'])
print(dfs1)
print('\t')
print(dfs1 + dfs2)
print('\t')
print(dfs1.add(dfs2,fill_value=0))



print('****************************')
ditcs = {
    'name':['zhansan','ana','bob'],
    'sex':['male','zhong','female'],
    'age':[11,12,32]
}
dfc = pd.DataFrame(ditc)
print(dfc)
print('\t')
print(dfc.iloc[1])
print('\t')
dfc.index = ['x1','x2','x3']
print(dfc)
print('\t')
print(dfc.loc['x2'])
print('\t')
print(dfc.ix['x2','name'])
print('\t')
print(dfc.ix[0])
print(dfc)
print('\t')
print(dfc.ix[['x2','x3'],'age'])
print('\t')
print(dfc.ix['x1':'x2','age'])