#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print (classmates)
print ('哈哈')
print (len(classmates))
# 用-1做索引，直接获取最后一个元素
print (classmates[-1])
# 追加classmates.append('ana')
# 插入classmates.insert(1,'oao') 把元素插入到指定的位置，比如索引号为1的位置
# 删除classmates.pop() 删除指定位置元素classmates.pop(i)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
# >>>t = (1,)
# >>>t 
# (1,)

# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

calc(1,2,3,4)

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['a','b','c']):
    print (i,value)


# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
[x * x for x in range(1, 11)]
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
[x *x for x in range(1,11) if x%2 ==0]

# 生成器
g = (x*x for x in range(10))
for n in g:
    print (n)

# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a+b
        n = n + 1
    return 'done'

# generator函数类型的写法
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print ('g:', x)
    except StopInteration as e:
        print ('Generator return value', e.value)
        break

