# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
# >>> print('\\\t\\')
# \       \
# >>> print(r'\\\t\\')
# \\\t\\

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
# >>> print('''line1
# ... line2
# ... line3''')
# line1
# line2
# line3

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

# >>> 9 / 3
# 3.0
# 还有一种除法是//，称为地板除，两个整数的除法仍然是整数：

# >>> 10 // 3
# 3

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：

# >>> print('包含中文的str')
# 包含中文的str
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

# >>> ord('A')
# 65
# >>> ord('中')
# 20013
# >>> chr(66)
# 'B'
# >>> chr(25991)
# '文'

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：

# x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：

# >>> 'Hello, %s' % 'world'
# 'Hello, world'
# >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# 'Hi, Michael, you have $1000000.'
# 你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。

# 常见的占位符有：

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

# >>> '%2d-%02d' % (3, 1)
# ' 3-01'
# >>> '%.2f' % 3.1415926
# '3.14'
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

# >>> 'Age: %s. Gender: %s' % (25, True)
# 'Age: 25. Gender: True'
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

# >>> 'growth rate: %d %%' % 7
# 'growth rate: 7 %'

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))



# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。/
# 函数对象有一个__name__属性，可以拿到函数的名字：
def now():
    print('2015-3-25')
f = now
f()

now._name_
f._name_

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# decorator就是一个返回函数的高阶函数。

def log(func):
    def wrapper(*arges,**kw):
        print ('call() %s():', % func._name_ )
        return func(**args,**kw)
    return wrapper

# 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
# @log
# def now():
#     print('2015-3-25')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

# >>> now()
# call now():
# 2015-3-25
# 把@log放到now()函数的定义处，相当于执行了语句：

# now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# 这个3层嵌套的decorator用法如下：

# @log('execute')
# def now():
#     print('2015-3-25')
# 执行结果如下：

# >>> now()
# execute now():
# 2015-3-25
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：

# >>> now = log('execute')(now)

# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

# >>> now.__name__
# 'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools 
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print ("%s %s ()" % (text,func._name_))
            return func(*args,**kw)
        return wrapper
    return decorator

