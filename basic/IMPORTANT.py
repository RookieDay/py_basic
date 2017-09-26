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


# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
# def int2(x, base=2):
#     return int(x, base)
# 这样，我们转换二进制就非常方便了：

# >>> int2('1000000')
# 64
# >>> int2('1010101')
# 85

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：

# >>> import functools
# >>> int2 = functools.partial(int, base=2)
# >>> int2('1000000')
# 64
# >>> int2('1010101')
# 85
# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：

# >>> int2('1000000', base=10)
# 1000000


# 判断对象类型，使用type()函数判断对象类型，使用type()函数
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

# 可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True

# @property装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
# ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']


# 模块
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# >>> from collections import namedtuple
# >>> Point = namedtuple('Point', ['x', 'y'])
# >>> p = Point(1, 2)
# >>> p.x
# 1
# >>> p.y
# 2


# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# >>> from collections import defaultdict
# >>> dd = defaultdict(lambda: 'N/A')
# >>> dd['key1'] = 'abc'
# >>> dd['key1'] # key1存在
# 'abc'
# >>> dd['key2'] # key2不存在，返回默认值
# 'N/A'

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
# from collections import OrderedDict

# class LastUpdatedOrderedDict(OrderedDict):
#     def __init__(self,capacity):
#         super(LastUpdatedOrderedDict,self).__init__()
#         self._capacity = capacity
#     del __setitem__(self,key,value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:',last)
#         if containsKey:
#             del self[key]
#             print('set:',(key,value))
#         else:
#             print('add:',(key,value))
#         OrderedDict.__setitem__(self,key,value)


# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

# >>> c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})  

# Base64是一种用64个字符来表示任意二进制数据的方法。
