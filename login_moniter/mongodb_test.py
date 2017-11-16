#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/14
# @Author  : RookieDay
# @Site    : 
# @File    : mongodb_test
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.ana
# db.col.insert({'name':'ana','age':11,'sex':'male'})
# db.col.insert([
#  {"name":'yanying','province':'江苏','age':25},
#  {"name":'张三','province':'浙江','age':24},
#  {"name":'张三1','province':'浙江1','age':25},
#  {"name":'张三2','province':'浙江2','age':26},
#  {"name":'张三3','province':'浙江3','age':28},
# ])
db.msk.insert({'name':'gl','age':11,'sex':'female'})
db.msk.insert([
 {"name":'yanying','province':'江苏','age':25},
 {"name":'张三','province':'浙江','age':24}
])

# print(db.col.find_one())
for item in db.col.find():
    print(item)