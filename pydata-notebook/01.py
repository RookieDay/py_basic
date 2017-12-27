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
# df1 = pd.DataFrame(np.arange(4).reshape(2,2),columns = ['a','b'])
# df2 = pd.DataFrame(np.arange(6).reshape(2,3),columns = ['a','b','c'])
# print(df1)
# print('*'*40)
# print(df1.iloc[1])
# print('*'*40)
# print(df1.loc[1])
# print('*'*40)
# print(df1.ix[0,'b'])

import matplotlib.pyplot as plt

# a = np.linspace(0, 2 * np.pi, 50)
# b = np.sin(a)
# plt.plot(a,b)
# mask = b >= 0
#
# plt.plot(a[mask], b[mask], 'bo')
# print(a)
# print(a[mask])
# plt.show()

# a = np.arange(0, 100, 10)
# b = np.where(a < 50)
# c = np.where(a >= 50)[0]
# print(a)
# print(b) # >>>(array([0, 1, 2, 3, 4]),)
# print(c) # >>>[5 6 7 8 9]
# print(a[b[0]])

#
# a1 = {'b': [1, 2, 3, 4],
#  'dummy': 'another value',
#  7: 'an integer',
#  'a': 'some value'}
#
# print(a1.pop('a'))
# print(a1)

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

# for word in words:
#     letter = word[0]
#     if letter not in by_letter:
#         by_letter[letter] = [word]
#     else:
#         by_letter[letter].append(word)


for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)

print(by_letter)



from collections import defaultdict
by_letter = defaultdict(list)
print(by_letter)
for word in words:
    by_letter[word[0]].append(word)
by_letter['x'].append('xx')
print(dict(by_letter))

print(hash((1, 2, (2, 3))))


# a = []
# def func():
#     for i in range(5):
#         a.append(i)
#
# print(a)


# def add_number(x, y):
#     return x + y
#
#
# from functools import partial
# add_five = partial(add_number, 5)
# print(add_five(13))

import itertools
first_letters = lambda x:x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
names = sorted(names,key=first_letters)
for letter, group in itertools.groupby(names,first_letters):
    print('{0} , {1}'.format(letter,list(group)))
    # print(letter, list(group))  # names is a generator
print('*'*50)
#
# for key, group in itertools.groupby('AAABBBCCAAACCC'):
#     print(key, list(group))
#
# def height_class(h):
#     if h>180:
#         return 'tall'
#     elif h<160:
#         return 'short'
#     else:
#         return 'middle'
#
# friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
#
# friends = sorted(friends,key = height_class)
#
# print(friends)

# str = "     this is string example....wow!!!ass     ";
# print(str.rstrip().rstrip('is'))
#
# a="rrbbrrddrr"
# b=a.strip("rr")
# print(b)
#
#
# x = np.empty((2, 3, 2), dtype=np.int32)
# print(x)
# print(x.ndim)
# print(x.shape)
#
#
# x = np.random.randn(7,4)
# print(x)
# x[x < 0] = 7
# print('*'*50)
# print(x)
#

arr = np.arange(32).reshape((8, 4))
print(arr)
print('*'*50)

print(arr[[-3,-5,-1,-2]])
print('*'*50)
print(arr[[1, 5, 7, 2]][ [0, 3, 1, 2]])
print('*'*50)
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])




arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print('*'*50)
print(arr.transpose((1, 0, 2)))
