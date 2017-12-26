#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/25
# @Author  : RookieDay
# @Site    : 
# @File    : README
# @Github  : https://github.com/rookieday
# @Software: PyCharm Community Edition

import numpy as np
# iloc是通过所在行的数字为索引，loc是所在行的标签为索引，简单讲，iloc是第几行，loc是标签。
# 当索引没有标签时，loc和iloc等价。两者支持冒号的范围选择。

# ix，则是两者的混合，即可以行号，也可以行索引
# df.ix['a','age'] 选择a行 ,列名为age的数值

# ix[ 行1:行2, 列1:列2 ]，iloc和loc也支持行列同时选择

# numpy.arange([start, ]stop, [step, ]dtype=None)

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# num 代表生成多少个数字
# endpoint 如果是真，则一定包括stop，如果为False，一定不会有stop
# retstep 如果威震 返回 (samples, step), step代表 数字之间的差值

# 数组的切片

# a[0,1:4] 选取数组下标第0行， 第1-4元素 不包括4
# a[1:4,0] 选取数组下标第1到3行 的第0个元素
# a[::2,::2] 选取数组行下标 0 2 4 对应列下标0 2 4 的元素
# a[:, 1] 选取数组全部行，列下标为1的元素 也就是选取下标1列

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

# a.itemsize --> 每一个条目所占的字节
# a.ndim     --> 指数组多少维
# a.nbytes   --> 表示这个数组中所有元素占用的字节数


# cumsum() 函数  ，第一个元素加到第二个元素上，把结果保存到一个列表里，然后把结果加到第三个元素上，再保存到列表里，依次累加。当遍历完数组中所有元素则结束，返回值为运行数组的总和的列表。
# np.array([1, 2, 3, 4, 5]).cumsum() = [1, 3, 6, 10, 15]

# where() 函数是另外一个根据条件返回数组中的值的有效方法。只需要把条件传递给它，它就会返回一个使得条件为真的元素的列表。
# Where
# a = np.arange(0, 100, 10)
# b = np.where(a < 50)
# c = np.where(a >= 50)[0]
# print(b) # >>>(array([0, 1, 2, 3, 4]),)
# print(c) # >>>[5 6 7 8 9]


# 取值
# seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# for a, b, c in seq:
#     print('a={0}, b={1}, c={2}'.format(a, b, c))
# a=1, b=2, c=3
# a=4, b=5, c=6
# a=7, b=8, c=9

# values = 1, 2, 3, 4, 5
# a, b, *rest = values
# rest部分是你想要丢弃的，名字本身无所谓，通常用下划线来代替：
# a, b, *_ = values

# list/tuple
# count用来计算某个值出现的次数，Tuple/list中也有这个方法
# insert方法运算量比append大。所以如果想要在序列的开头和结尾添加元素的话，可以使用collections.deque，这是一种双结尾的队列 insert的反向操作较pop, 能移除序列中特定位置的元素：
# 用+法来做合并是一个运算量较大的操作，因为要创建一个新的list并复制。如果操作的是一个很大的list，用extend会更好一些：

# append是把元素添加到一个list里
# extend是把两个list结合在一起
# +是创建了一个新的list并返回，运算量大
# extend是在原本的list上做了更改，运算量小

# 用-1能反转一个list或tuple：
# seq[::-1]

# enumerate通常用来把一个list中的位置和值映射到一个dcit字典里
# sl = ['foo','bar','baz']
# mapp = {}
# for i,v in enumerate(sl):
#     mapp[v] = i

# sorted函数返回一个新的排好序的序列，而之前提到的.sort方法是直接更改原有的序列，不产生新序列
# zip 用于"pairs"(成对)。把多个序列中每个对应的元素变成一对，最后返回一个含有tuple的list
# seq1 = ['foo', 'bar', 'baz']
# seq2 = ['one', 'two', 'three']
# zippped = zip(seq1,seq2)
# list(zippped)
# 输出 ： [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
# zip可以接收任意长度的序列，最后返回的结果取决于最短的序列
# seq3 = [False, True]
# list(zip(seq1, seq2, seq3))
# 输出： [('foo', 'one', False), ('bar', 'two', True)]

# zip的一个常见用法是同时迭代多个序列，可以和enumerate搭配起来用：
# for i, (a,b) in enumerate(zip(seq1,seq2)):
#     print('{0}: {1}, {2}'.format(i,a,b))
# 0: foo, one
# 1: bar, two
# 2: baz, three

# 如果给我们一个压缩过的序列，我们可以将其解压
# pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),
#             ('Schilling', 'Curt')]
# first_names, last_names = zip(*pitchers)


# 从序列中生成dict
# mapping = dict(zip(range(5), reversed(range(5))))
# {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}

# 一个dict中的value也是其他集合，比如list。举例说明，我们想要把一些单词按首字母归类：
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

# 输出{'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

# 可以使用setdefault方法进行改写
# 使用setdefault() 初始化字典键值. 使用字典的时候经常会遇到这样一种应用场景：动态更新字典，像如上面代码，如果key不在dictionary 中那么就添加它并把它对应的值初始为空列表[] ，然后把元素append到空列表中。
for word in words:
    letter = word[0]
    by_letter.setdefault(letter,[]).append(word)

# 内建的collections模块有一个有用的class，defaultdict，这个能让上述过程更简单。创建方法是传递一个type或是函数：
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)


# Valid dict key types(有效的key类型)
# 通常key的类型是不可更改的常量类型（int，float，string）或tuple。专业的叫法是hashability。可以查看一个object是否是hashable，只要是hashable的，就可以当做dict中的key。这里用hash函数查看：
hash((1, 2, (2, 3)))  #1097636502276347782
hash(1, 2, [2, 3]) # 失败，因为list是可变的


# set是无序且元素不重复的。就像是key唯一，且没有value的字典。两种方式可以创建，一个是用set函数，一个是用花括号：
# set([2, 3, 2, 1, 4, 4, 3])
# -->
# {1, 2, 3, 4}
#
# {2, 3, 2, 1, 4, 4, 3}
# -->
# {1, 2, 3, 4}

# a.union(b) /  a.intersection(b) /a & b