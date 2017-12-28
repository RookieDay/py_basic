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
# arr = np.arange(16).reshape((2, 3, 4))
# arr.shape -- (2,3,4) 对应索引(0,1,2)
# arr.transpose((1,0,2)) 就会变为 x.shape -- (3,2,4)
# arr.swapaxes(1, 2) # 原来shape(2,3,4)现在变为了(2,4,3) 只交换second axis和last axis swapaxes也是返回view，不生成新的data。


# modf 函数 实现a除以b，然后返回商与余数的元组。如果两个参数a,b都是整数，那么会采用整数除法，结果相当于（a//b, a % b)。如果a或b是浮点数，相当于（math.floor(a/b), a%b)。
# arr = np.random.randn(7)*5
# remainder, whole_part = np.modf(arr)
# whole_part

# [X,Y] = meshgrid(x,y) 将向量x和y定义的区域转换成矩阵X和Y,其中矩阵X的行向量是向量x的简单复制，而矩阵Y的列向量是向量y的简单复制
# 假设x是长度为m的向量，y是长度为n的向量，则最终生成的矩阵X和Y的维度都是 nm （注意不是mn）

# numpy.where函数是一个向量版的三相表达式，x if condition else y
# np.where中第二个和第三个参数不用必须是数组。where在数据分析中一个典型的用法是基于一个数组，产生一个新的数组值
# 假设我们有一个随机数字生成的矩阵，我们想要把所有的正数变为2，所有的负数变为-2。用where的话会非常简单：
# arr = np.random.randn(4, 4)
# np.where(arr > 0, 2, -2)
# 以结合标量和数组。比如只把整数变为2，其他仍未原来的数字
# np.where(arr > 0, 2, arr) # set only positive value to 2


# 一些能计算统计值的数学函数能基于整个数组，或者沿着一个axis（轴）。可以使用aggregations(often called reductions，汇总，或被叫做降维)，比如sum, mean, and std(标准差).
# mean, sum这样的函数能接受axis作为参数来计算统计数字，返回的结果维度更少
# arr.sum(axis=0) 计算各行总和
# arr.mean(axis=1) 计算各列之间的平均值
# arr.cumsum()  计算是一个累加的结果
# arr.cumsum(axis=0) # 沿着行加法
# arr.cumprod(axis=1) # 沿着列乘法

# sum是用来计算布尔数组中有多少个true
# (arr > 0).sum()
# any检测数组中只要有一个ture返回就是true，而all检测数组中都是true才会返回true
# bools = np.array([False, False, True, False])
# bools.any()  true
# bools.all()  false

# 直接调用数组的sort方法，会改变原有数组的顺序。但如果使用np.sort()函数的话，会生成一个新的排序后的结果
# arr = np.random.randn(5, 3)
# arr.sort(1)

# np.unique，能返回排好序且不重复的值
# ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
# np.uniques(ints)
# python 实现sorted(set(names))

# np.in1d, 测试一个数组的值是否在另一个数组里，返回一个布尔数组
# np.linalg能用来做矩阵分解，以及比如转置和求秩之类的事情
# X = np.round(np.random.randn(5, 5), 3) #用np.round控制小数点后的位数
# X.T.dot(X)计算的是X和X的转置的矩阵乘法。

# np.linalg能用来做矩阵分解，以及比如转置和求秩之类的事情
# np.linalg.inv()：矩阵求逆
# np.linalg.det()：矩阵求行列式（标量）
# np.linalg.norm 求范数  norm(x, ord=None, axis=None, keepdims=False)
# normal得到一个4 x 4的，符合标准正态分布的数组 np.random.normal(size=(4, 4))

# np.random.seed(1)
# 只要seed设置一样，每次生成的随机数是相同的
# 这个seed是全局的，如果想要避免全局状态，可以用numpy.random.RandomState来创建一个独立的生成器
# rng = np.random.RandomState(1234)
# rng.randn(10)


# argmax来计算，这个会返回布尔数组中最大值的索引(Ture是最大值)
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
# print(np.argmax(a, axis=0)) 行间比较 输出-array([1, 2, 2, 1])

a = np.array([[1, 5, 5, 9],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
# print(np.argmax(a, axis=1))  列间比较 输出array([3, 0, 2])

# numpy.random.randint(low,high=None,size=None,dtype)
# 生成在半开半闭区间[low,high)上离散均匀分布的整数值;若high=None，则取值区间变为[0,low)

import pandas as pd

# padndas
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon':16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
# 顺序是按states里来的，但因为没有找到california,所以是NaN。NaN表示缺失数据,isnull和notnull函数可以用来检测缺失数据：

# Series自身和它的index都有一个叫name的属性
obj4.name = 'population'
obj4.index.name = 'state'
#
# obj4
# state
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# Name: population, dtype: float64
#
# series的index能被直接更改：

# 指定按列排序
# pd.DataFrame(data, columns=['year', 'state', 'pop'])
# 导入一个不存在的列名，那么会显示为缺失数据

# 如果把list或array赋给column的话，长度必须符合DataFrame的长度。如果把一二series赋给DataFrame，会按DataFrame的index来赋值，不够的地方用缺失数据来表示
# list赋值
# frame2['debt'] = np.arange(6.)
# series赋值
# val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# frame2['debt'] = val

# frame3.T 可转置

# DataFrame的index和column有自己的name属性，也会被显示
# frame3.index.name = 'year'; frame3.columns.name = 'state'


# pandas的Index Objects (索引对象)负责保存axis labels和其他一些数据（比如axis name或names）。一个数组或其他一个序列标签，只要被用来做构建series或DataFrame，就会被自动转变为index
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
# index -->Index(['a', 'b', 'c'], dtype='object')
# index object是不可更改的
# 正因为不可修改，所以data structure中分享index object是很安全的
labels = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
# obj2.index is labels -- >true


