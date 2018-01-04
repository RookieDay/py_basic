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


# reindex 重新索引
# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# d    4.5
# b    7.2
# a   -5.3
# c    3.6
# dtype: float64

# 在series上调用reindex能更改index，如果没有对应index的话会引入缺失数据
# obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

# 在处理时间序列这样的数据时，我们可能需要在reindexing的时候需要修改值。method选项能做到这一点，比如设定method为ffill
# obj3 = pd.Series(['bule', 'purple', 'yellow'], index=[0, 2, 4])
# obj3.reindex(range(6), method='ffill')


# 对于DataFrame，reindex能更改row index,或column index。reindex the rows
frame = pd.DataFrame(np.arange(9).reshape(3, 3),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
# index
frame2 = frame.reindex(['a', 'b', 'c', 'd'])

# 列
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

# 还可以使用loc更简洁的reindex
frame.loc[['a', 'b', 'c', 'd'], states]


# 对于series，drop会返回一个新的object，并删去你制定的axis的值
# 对于DataFrame，index能按行或列的axis来删除
# data.drop(['Colorado', 'Ohio']) 删除行
# data.drop('two', axis=1) 列处理：drop列的话，设定axis=1或axis='columns':
# data.drop(['two', 'four'], axis='columns')
# obj.drop('c', inplace=True) drop也可以不返回一个新的object，而是直接更改series or dataframe in-place

# loc and iloc. 这两个方法能通过axis labels(loc)或integer(iloc)，来选择行或列
# data
# 	       one	two	three	four
# Ohio	    0	0	0	    0
# Colorado	0	5	6	    7
# Utah	    8	9	10	    11
# New York	12	13	14	    15
# data.loc['Colorado', ['two', 'three']] Colorado行的two three列值
# data.iloc[1, [1, 2]] 同iloc实现相同的效果
# 切片
# data.loc[:'Utah', 'two'] 到'utah'行,取'two'列的值
# data.iloc[:, :3][data.three > 5] 所有行的第0-2列 比data.three大于5的


# pandas在整数索引上可能会出错,如果用非整数来做index，就没有歧义了
# ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
# ser2[-1]
# ser[:1]
# df1.add(df2, fill_value=0)
# df1.reindex(columns=df2.columns, fill_value=0)  reindex（重建索引）的时候，也可以使用fill_value
# 1 / df1  -- > 逆运算  df1.rdiv(1)

# frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
#                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# 把一个用在一维数组上的函数，应用在一行或一列上。要用到DataFrame中的apply函数
# f = lambda x: x.max() - x.min()
# frame.apply(f)
# frame.apply(f, axis=1)

# def f(x):
#     return pd.Series([x.min(), x.max()], index=['min', 'max'])
# frame.apply(f,axis=1)

# element-wise的python函数也能用。假设想要格式化frame中的浮点数，变为string。可以用apply map
# series有一个map函数，能用来实现element-wise函数
# format = lambda x: '%.2f' % x
# frame.applymap(format)
# frame['e'].map(format)


# 按row或column index来排序的话，可以用sort_index方法，会返回一个新的object
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()

# 在DataFrame，可以用index或其他axis来排序
# frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
#                      index=['three', 'one'],
#                      columns=['d', 'a', 'b', 'c'])
# frame
# frame.sort_index(axis=1)
# 默认是升序，可以设置降序
# frame.sort_index(axis=1, ascending=False)

# 通过值来排序，用sort_values方法,缺失值会被排在最后
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
obj.sort_values()


# 对于一个DataFrame，可以用一列或多列作为sort keys。这样的话，只需要把一列多多列的名字导入到sort_values即可,多列排序的话，传入一个list of names
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame.sort_values(by='b')
frame.sort_values(by=['a', 'b'])
# ranking（排名）是给有效的数据分配数字。rank方法能用于series和DataFrame，rank方法默认会给每个group一个mean rank（平均排名）。rank 表示在这个数在原来的Series中排第几名，有相同的数，取其排名平均（默认）作为值
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()
# rank也可以根据数据被观测到的顺序来设定
# obj.rank(method='first')

# index的is_unique特性能告诉我们label是否是唯一的
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj.index.is_unique
# 数据选择对于重复label则表现有点不同。如果一个label有多个值，那么就会返回一个series, 如果是label只对应一个值的话，会返回一个标量
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df.loc['b']

# 可以用skipna来跳过计算NA
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
df.mean(axis=1, skipna=False)

# idxmin和idxmax，能返回间接的统计值，比如index value
# df.idxmax() 最大值索引
#     one   two
# a	1.40	NaN
# b	7.10	-4.5
# c	NaN	    NaN
# d	0.75	-1.3
# df.idxmax()
# one    b
# two    d
# dtype: object

# describe能一下子产生多维汇总数据
# pct_change(): 这个函数用来计算同colnums两个相邻的数字之间的变化率
# series的corr方法计算两个，重合的，非NA的，通过index排列好的series。cov计算方差
# 用Dataframe的corrwith方法，我们可以计算dataframe中不同columns之间，或row之间的相似性。传递一个series

# pd.read_table('../examples/ex1.csv', sep=',') sep指定分割符
# 读取没有header的文件  pd.read_csv('../examples/ex2.csv', header=None)
# 可以为其设置列名:pd.read_csv('../examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
# 可以传入一个正则表达式给read_table来代替分隔符。用正则表达式为\s+ result = pd.read_table('../examples/ex3.txt', sep='\s+')
# pd.read_csv('../examples/ex4.csv', skiprows=[0, 2, 3]) 跳过不规整的数据
# 对于缺失值，pandas使用一些sentinel value(标记值)来代表，比如NA和NULL pd.isnull(result)
# na_values选项能把我们传入的字符识别为NA，导入必须是list result = pd.read_csv('../examples/ex5.csv', na_values=['NULL'])
# 可以给不同的column设定不同的缺失值标记符，这样的话需要用到dict
sentinels = {'message': ['foo', 'NA'],
             'something': ['two']}
# 把message列中的foo和NA识别为NA，把something列中的two识别为NA
pd.read_csv('../examples/ex5.csv', na_values=sentinels)


# pd.read_csv('../examples/ex6.csv', nrows=5) 读取前几行（不读取整个文件），指定一下nrows
# 读取文件的一部分，可以指定chunksize chunker = pd.read_csv('../examples/ex6.csv', chunksize=1000)
# pandas返回的TextParser object能让我们根据chunksize每次迭代文件的一部分。比如，我们想要迭代ex6.csv, 计算key列的值的综合
chunker = pd.read_csv('../examples/ex6.csv', chunksize=1000)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)
# TextParser有一个get_chunk方法，能返回任意大小的数据片段： chunker.get_chunk(10)

# data.to_csv(sys.stdout, sep='|')
# 缺失值会以空字符串打印出来，我们可以自己设定缺失值的指定符  data.to_csv(sys.stdout, na_rep='NULL')
# 如果不指定，行和列会被自动写入。当然也可以设定为不写入  data.to_csv(sys.stdout, index=False, header=False)
# 可以指定只读取一部分列，并按你选择的顺序读取 data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])


# 有时候需要人为处理的数据
# header, values = lines[0], lines[1:]
# data_dict = {h: v for h, v in zip(header, zip(*values))}
# print([x for x in zip(*values)])

# CSV有很多功能。我们可以定义一个新的分隔符格式，比如字符串的引号，行结束时的回车，这里我们利用csv.Dialect来构造一个子类
# class my_dialect(csv.Dialect):
#     lineterminator = '\n'
#     delimiter = ';'
#     quotechar = '"'
#     quoting = csv.QUOTE_MINIMAL
#
# f = open('../examples/ex7.csv')
# reader = csv.reader(f, dialect=my_dialect)
# 也可以设定一个分隔符参数给csv.reader，而不用单独定义一个子类 csv.reader(f, delimiter='|')

# pandas.read_html函数有很多额外选项，但是默认会搜索并试图解析含有<tagble>tag的表格型数据。结果是a list of dataframe:
# json/csv
# close_timestamps = pd.to_datetime(failures['Closing Date'])
# close_timestamps.dt.year.value_counts()

# 使用lxml.objectify,我们可以解析文件，通过getroot，得到一个指向XML文件中root node的指针
# from lxml import objectify
#
# parsed = objectify.parse(open(path))
# root = parsed.getroot()

# 解析root 循环children 放入data = [] 然后变为DataFrame
# perf = pd.DataFrame(data)
# perf.head()

# 用内建的pickle可以直接读取任何pickle文件，或者直接用pandas.read_pickle
# pickle只推荐用于短期存储。因为这种格式无法保证长期稳定；比如今天pickled的一个文件，可能在库文件更新后无法读取。

# HDFStore支持两种存储架构，fixed和table。后者通常更慢一些，但支持查询操作
# store = pd.HDFStore('../examples/mydata.h5')
# store.put('obj2', frame, format='table')
# store.select('obj2', where=['index >= 10 and index <= 15'])
# pd.read_hdf('./examples/mydata.h5', 'obj3', where=['index < 5'])
# 注意：HDF5不是数据库（database）。它最适合一次写入，多次读取的数据库。尽管数据可以在任何时间多次写入一个文件，如果多个使用者同时写入的话，文件会被破坏。

# 读取excel xlsx = pd.ExcelFile('../examples/ex1.xlsx')  ->pd.read_excel(xlsx, 'Sheet1')
# 读取sheet frame = pd.read_excel('../examples/ex1.xlsx', 'Sheet1')
# pandas数据写为Excel格式  writer = pd.ExcelWriter('../examples/ex2.xlsx') frame.to_excel(writer, 'Sheet1') writer.save()
# 如果不适用ExcelWriter的话，可以直接传给to_excel一个path：frame.to_excel('../examples/ex2.xlsx')

# import requests
# url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
# resp = requests.get(url)
# data = resp.json()
# # 提取感兴趣信息
# issues = pd.DataFrame(data, columns=['number', 'title',
#                                     'labels', 'state'])
# issues

# 数据库 sqlite3
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""
con = sqlite3.connect('./examples/mydata.sqlite')
con.execute(query)
con.commit()
cursor = con.execute('select * from test')
rows = cursor.fetchall()
# 使用sqlalchemy

# 处理缺失值 内建的Python None值也被当做NA
# string_data.isnull()
# data = pd.Series([1, NA, 3.5, NA, 7])
# data.dropna()  等价于--> data[data.notnull()]
# dropna默认会删除包含有缺失值的row
# data.dropna(how='all') how=all只会删除那些全是NA的行
# 删除列也一样，设置axis=1 data.dropna(axis=1, how='all')

# 保留有特定数字的观测结果，可以使用thresh参数
from numpy import nan as NA
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df.dropna()
df.dropna(thresh=2)

df.fillna(0)
df.fillna({1: 0.5, 2: 0}) #给fillna传入一个dict，可以给不同列替换不同的值
_ = df.fillna(0, inplace=True) # fillna返回一个新对象，但你可以使用in-place来直接更改原有的数据
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)

data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean()) #可以传入一个series的平均值或中位数

# 删除重复行
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
data.duplicated() #duplicated返回的是一个boolean Series，表示一个row是否是重复的（根据前一行来判断）
data.drop_duplicates() # drop_duplicateds返回一个DataFrame，会删除重复的部分
data.drop_duplicates(['k1', 'k2'], keep='last') # 设置keep='last'能返回最后一个


# 函数映射  使用map函数  方便很多
# data['food'].map(lambda x: meat_to_animal[x.lower()])
# 替换 data.replace(-999, np.nan)
# data.replace([-999, -1000], np.nan) 如果想要一次替换多个值，直接用一个list
# data.replace({-999: np.nan, -1000: 0})

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()
data.index = data.index.map(transform)

# 创建一个转换后的版本，而且不用修改原始的数据，可以用rename
data.rename(index=str.title, columns=str.upper)
# rename能用于dict一样的oject
data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'pekaboo'})
# 可以用inplace直接修改原始数据
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)


ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# 把这些分到四个bin里，19~25, 26~35, 36~60, >60。可以用pandas里的cut
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
# [(18, 25], (18, 25], (18, 25], (25, 35], ...
# Length: 12
# Categories (4, object): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]
# 返回的是一个特殊的Categorical object,结果描述了pandas.cut如何得到bins。可以看作是一个string数组用来表示bin的名字，它内部包含了一个categories数组，用来记录不同类别的名字，并伴有表示ages的label（
cats.codes #表示ages的label
cats.categories
pd.value_counts(cats) #pd.value_counts(cats)是pandas.cut后bin的数量
# 括号表示不包含，方括号表示包含。你可以自己设定哪一边关闭（right=False）
# pd.cut(ages, [18, 26, 36, 61, 100], right=False)
# 输出
# [[18, 26), [18, 26), [18, 26), [26, 36), [18, 26), ..., [26, 36), [61, 100), [36, 61), [36, 61), [26, 36)]
# Length: 12
# Categories (4, object): [[18, 26) < [26, 36) < [36, 61) < [61, 100)]

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)


# 如果你只是给一个bins的数量来cut，而不是自己设定每个bind的范围，cut会根据最大值和最小值来计算等长的bins。比如下面我们想要做一个均匀分布的四个bins
pd.cut(data, 4, precision=2)  # 表示数据分为4个均匀分布的bins

# 一个近似的函数，qcut，会按照数据的分位数来分箱。取决于数据的分布，用cut通常不能保证每一个bin有一个相同数量的数据点。而qcut是按百分比来切的，所以可以得到等数量的bins
cats = pd.qcut(data, 4) # Cut into quartiles

cats2 = pd.cut(data, [0, 0.1, 0.5, 0.9, 1.]) # 累进的百分比 在cut中我们可以自己指定百分比


data = pd.DataFrame(np.random.randn(1000, 4))
data.describe()
col = data[2]
col[np.abs(col) > 3]

# 选中所有绝对值大于3的行，可以用any方法在一个boolean DataFrame上
data[(np.abs(data) > 3)].head()
data[(np.abs(data) > 3).any(1)] # any中axis=1表示column
data[np.abs(data) > 3] = np.sign(data) * 3 # 绝对值大于3的数字直接变成-3或3
np.sign(data).head() # np.sign(data)会根据值的正负号来得到1或-1


# 排列（随机排序）一个series或DataFrame中的row，用numpy.random.permutation函数很容易就能做到。调用permutation的时候设定好你想要进行排列的axis，会产生一个整数数组表示新的顺序
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
# 这个数组能被用在基于iloc上的indexing或take函数
sampler = np.random.permutation(5) #array([4, 3, 2, 1, 0])
df.take(sampler) #df会根据sampler打乱索引排列
# 为了选中一个随机的子集，而且没有代替功能(既不影响原来的值，返回一个新的series或DataFrame)，可以用sample方法
df.sample(n=3)  #会随机选择三行
# 如果想要生成的样本带有替代功能(即允许重复)，给sample中设定replace=True
choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)


# 如果DataFrame中的一列有k个不同的值，我们可以用一个矩阵或DataFrame用k列来表示，1或0。pandas有一个get_dummies函数实现这个工作，当然，你自己设计一个其实也不难。
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})
#
# data1	key
# 0	0	b
# 1	1	b
# 2	2	a
# 3	3	c
# 4	4	a
# 5	5	b

# 对于上面的key列 0 1 来分
pd.get_dummies(df['key'])
#
#     a	b	c
# 0	0.0	1.0	0.0
# 1	0.0	1.0	0.0
# 2	1.0	0.0	0.0
# 3	0.0	0.0	1.0
# 4	1.0	0.0	0.0
# 5	0.0	1.0	0.0

# 如果我们想要给column加一个prefix， 可以用data.get_dummies里的prefix参数来实现
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)


# 假如我们这里操作一个数据集，某一列它里面类别有很多
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('./datasets/movielens/movies.dat', sep='::',
                       header=None, names=mnames, engine='python')
movies[:10]

# 获取所有的类别放在数组里面
all_genres = []

for x in movies.genres:
    all_genres.extend(x.split('|'))
# 类别去重
genres = pd.unique(all_genres)

# 构建一个全是0的 DataFrame，并且列为不同的类别
zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)
dummies.head()

# 循环类别 在dummies 获取对应的下标位置是哪个 ，使用.iloc，根据索引来设定值
for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1

# 然后我原来的结合在一起
movies_windic = movies.join(dummies.add_prefix('Genre_'))
movies_windic.iloc[0]


# 对于一个很大的数据集，这种构建多个成员指示变量的方法并不会加快速度。写一个低层级的函数来直接写一个numpy array，并把写过整合到DataFrame会更快一些
np.random.seed(12345)
values = np.random.randn(10)
bins = [0,0.2,0.4,0.6,0.8,1.]
pd.get_dummies(pd.cut(values,bins))


# 当调用re.split('\s+', text)的时候，正则表达式第一次被compile编译，并且split方法会被调用搜索text。我们可以自己编译regex，用re.compile，可以生成一个可以多次使用的regex object
# re.split('\s+', text)
# import re
# regex = re.compile('\s+')
# regex.split(text)

# match和search，与findall关系紧密。不过findall会返回所有匹配的结果，而search只会返回第一次匹配的结果 更严格地说，match只匹配string开始的部分。
# re.IGNORECASE makes the regex case-insensitive
# regex = re.compile(pattern, flags=re.IGNORECASE)
# regex.findall(text) 使用findall找到一组


# 而sub返回一个新的string，把pattern出现的地方替换为我们指定的string
# print(regex.sub('REDACTED', text))

# search返回text中的第一个匹配结果。match object能告诉我们找到的结果在text中开始和结束的位置
# m = regex.search(text)
# text[m.start():m.end()]
# regex.match返回None，因为它只会在pattern存在于stirng开头的情况下才会返回匹配结果

# m = regex.match('wesm@bright.net')
# m.groups()
# \1表示第一个匹配的group，\2表示第二个匹配的group
# print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))


# 可以把一些字符串方法和正则表达式（用lambda或其他函数）用于每一个value上，通过data.map，但是这样会得到NA(null)值。为了解决这个问题，series有一些数组导向的方法可以用于字符串操作，来跳过NA值。这些方法可以通过series的str属性；比如，我们想检查每个电子邮箱地址是否有'gmail' with str.contains:
# data = pd.Series(data)
# data.str.findall(pattern, flags=re.IGNORECASE)
#
# matches = data.str.match(pattern, flags=re.IGNORECASE)
# matches.str.get(0)
# data.str[:5]


# 分层索引的数据
data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
# data
# Out[4]:
# a  1    0.636082
#    2   -1.413061
#    3   -0.530704
# b  1   -0.041634
#    3   -0.042303
# c  1    0.429911
#    2    0.783350
# d  2    0.284328
#    3   -0.360963
# dtype: float64
data['b': 'c']
data.loc[['b','d']]
data.loc[:, 2]
# Out[9]:
# a   -1.413061
# c    0.783350
# d    0.284328
# dtype: float64

# 分层索引的作用是改变数据的形状，以及做一些基于组的操作（group-based）比如做一个数据透视表（pivot table）。例子，我们可以用unstack来把数据进行重新排列，产生一个DataFrame
data.unstack()
#         1	        2	        3
# a	0.636082	    -1.413061	-0.530704
# b	-0.041634	    NaN	        -0.042303
# c	0.429911	    0.783350	NaN
# d	NaN	            0.284328	-0.360963

# 相反的操作是stack:
data.unstack().stack()


frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame

# 	Ohio	Colorado
#   Green	Red	Green
# a	1	0	1	2
#   2	3	4	5
# b	1	6	7	8
#   2	9	10	11

# 每一层级都可以有一个名字（字符串或任何python对象）。如果有的话，这些会显示在输出中
frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']

#       state	        Ohio	Colorado
#       color	Green	Red	    Green
#key1	key2
# a	    1	    0	    1	    2
#       2	    3       4	    5
# b	    1	    6	    7	    8
#       2	    9	    10  	11

# 如果想要选中部分列(partial column indexing)的话，可以选中一组列（groups of columns）
frame['Ohio']
# 	    color	Green	Red
# key1	key2
# a	    1	    0	    1
#       2	    3	    4
# b   	1	    6	    7
#       2	    9	    10

# MultiIndex能被同名函数创建，而且可以重复被使用；在DataFrame中给列创建层级名可以通过以下方式
pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
                      names=['state', 'color'])

