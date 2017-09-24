#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'student object (name = %s)' % self.name
    __repr__ = __str__
print (Student('Michael'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    
# 一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。    
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
# >>> list(range(100))[5:10]
# [5, 6, 7, 8, 9]
    def __getitem__(self,n):
        if isinstance(n,int):    
            a,b = 1,1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(x,slice): 
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L =[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

for n in Fib():
    print(n)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(name, '=>', member, member.value)