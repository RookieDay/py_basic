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


strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
loc_mapping = {val: index for index, val in enumerate(strings)}
# 输出：{'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}


some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
# flattened [1, 2, 3, 4, 5, 6, 7, 8, 9]

# || 等价于
flatteded = []

for tup in some_tuples:
    for x in tup:
        flattened.append(x)


# 列表表达式里再有一个列表表达式也是可以的，可以生成a list of lists：
[[x for x in tup] for tup in some_tuples]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# 按不同字母的数量给一组string排序
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x:len(set(list(x))))

# 柯里化（Currying）是把接受多个参数的函数变换成接受一个单一参数(最初函数的第一个参数)的函数，并且返回接受余下的参数且返回结果的新函数的技术。
# 简单的说，通过局部参数应用，在一个原有函数的基础上，构造一个新的函数。
def add_number(x, y):
    return x + y

# 通过上面这个函数，我们可以衍生出一个只需要一个参数的新方程，add_five，即把5加到参数上：
add_five = lambda y: add_number(5, y)

# 其中第二个参数y叫做被柯里化了。这其实没什么特别的，我们做的其实就是用一个已有的函数定义了一个新函数。而内建的functools模块里的partial函数能简化这个操作
from functools import partial
add_five = partial(add_number, 5)


# 生成器是用于构造迭代对象的简洁方式。不像其他函数一口气执行完，返回一个结果，生成器是多次返回一个序列，每请求一次，才会返回一个。用yield可以构建一个生成器
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(1, n+1):
        yield i ** 2
gen = squares()
for x in gen:
    print(x, end=' ')

# 另一个构造生成器的方式是利用生成器表达式。写法就像列表表达式一样，只不过使用括号：
gen = (x ** 2 for x in range(100))
def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

# 生成器表达式还能作为函数的参数，而列表表达式不能作为函数的参数：
sum( x ** 2 for x in range(100))
dict((i, i**2) for i in range(5))
#输出： {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# itertools module¶

# 异常处理
# f = open(path, 'w')
#
# try:
#     write_to_file(f)
# except:
#     print('Failed')
# else:
#     print('Succeeded')
# finally:
#     f.close()


# 没有参数代表去除  两边 左边 右边的空格
# strip() 去除两端 如果传入了字符，会将字符串两边的字符都去掉
# lstrip() 去除左边 如果传入了字符，会将字符串左边的字符都去掉
# rstrip() 去除右边 如果传入了字符，会将字符串右边的字符都去掉

# 字符串，那些你不知道的事
# http://liujiacai.net/blog/2015/11/20/strings/

# np.empty并不能保证返回所有是0的数组，某些情况下，会返回为初始化的垃圾数值


# arr2d[:2, 1:] # 前两行，第二列之后
# arr2d[:2, 2]  #选中第三列的前两行
# arr2d[:, :1] #冒号表示提取整个axis（轴）：

# 用布尔索引总是会返回一份新创建的数据，原本的数据不会被改变
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

data = np.random.randn(7, 4)
# 假设每一个name对应data数组中的一行，我们想要选中name为'Bob'的所有行。就像四则运算，用比较运算符（==）
data[names == 'Bob']
# array([[ 0.02584271, -1.53529621,  0.73143988, -0.34086189],
#        [-0.48632936,  0.63817756, -0.40792716, -1.48037389]])
# 注意：布尔数组和data数组的长度要一样。
# 我们可以选中names=='Bob'的行，然后索引列

# Fancy Indexing(花式索引)¶
arr = np.arange(32).reshape((8, 4))
# 注意这里的括号
# arr[[1, 5, 7, 2], [0, 3, 1, 2]]
# -->array([ 4, 23, 29, 10])
# 可以看到[ 4, 23, 29, 10]分别对应(1, 0), (5, 3), (7, 1), (2, 2)。不论数组有多少维，fancy indexing的结果总是一维
# arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] ， 先从arr中选出[1, 5, 7, 2]这四行，然后[:, [0, 3, 1, 2]]表示选中所有行，但是列的顺序要按0,3,1,2来排。

# 转置 一个是transpose方法，一个是T属性
# 对于多维数组，transpose会接受由轴数字组成的tuple，来交换轴
