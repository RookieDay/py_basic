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