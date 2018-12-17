'''
    1  lambda 函数
    2  生成器不保留迭代过后的结果
    3  可变对象不能作为函数默认值
    4  在循环中修改列表选项
    5  列表取值超出索引数
    6  重用全局变量
    7  拷贝可变对象
    8  Python 多继承
    9  列表的 append 和 extend
    10 datetime 布尔值
    11 == & is 区别
    12 copy deepcopy pickle
    13 list 操作技巧
    14 dict 操作技巧
    15 Python yield
    16 异常处理
    17 Python 三种方法
    18 Python 三器
    19 属性监听
    20 异步调用
    
'''
# 1
my_list = [lambda x: x*i for i in range(5)]
for m in my_list:
    print(m(1)) # 4,4,4,4,4

# 输出[0,1,2,3,4] 方法一
my_list1 = [lambda x, i=i: x*i for i in range(5)]
for m in my_list1:
    print(m(1))
# 方法二：生成器
my_gen = (lambda x: x*i for i in range(5))
for m in my_gen:
    print(m(1))
# 方法三：将方法一改写为def函数，即闭包函数
def func():
    lst = []
    for i in range(5):
        def bar(x, i=i):
            return x*i
        lst.append(bar)
    return lst
for m in func():
    print(m(1))

# 方法四：Zip()方法
def func(items, num):
    return zip(*[iter(items)]*num)
print(func(range(9), 3))

# 2
gen = (i for i in range(5))
print(2 in gen)  # True
print(3 in gen)  # True
print(1 in gen)  # False 调用1->2, 这时1不在genrater中，按循环顺序，按需生成

gen1 = (i for i in range(5))
lst = list(gen1)
print(2 in lst)
print(3 in lst)
print(1 in lst)  # 均为 True，因为list会保存值，循环过，一样在

# 3
def foo(value, list=[]):
    list.append(value)
    return list
l1 = foo(1)
print(l1)         # [1]
l2 = foo(2)
print(l2)         # [1,2]

# 修改函数只取[2]
def foo1(value, num=None):
    if num is None:
        num = []
    num.append(value)
    return num
l1 = foo1(1)
print(l1)         # [1]
l2 = foo1(2)
print(l2)         # [2]

import time

def report_arg(_default=time.time()):
    print(_default)
report_arg()      # 1543575193.180959
time.sleep(2)
report_arg()      # 1543575193.180959
# 字典，列表，集合等对象不适合做函数默认值，因为默认值会在函数建立时生成，每次都是调用了对象的 ‘缓存’

# 4
a = list(range(30))
for i in a:
    if i%4 !=0:
        a.remove(i)
print(a)          # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

import copy
a = list(range(30))
b = copy.deepcopy(a)
for i in a:
    if i%4 !=0:
        b.remove(i)
print(b)          # [0, 4, 8, 12, 16, 20, 24, 28]
# for in 是对下biao进行操作，remove()是对值进行操作

# 5 
lst = [1,2,3,4,5]
# print(lst[5])
print(lst[5:])    # []

# 6

# 7
lst = [[1,2,3]] *2
lst2 = [[1,2,3] for i in range(2)]
print(lst)
print(lst2)

lst[1][0] = 'a'
print(lst)
lst2 = [[1,2,3] for i in range(2)]
lst2[1][0] = 'a'
print(lst2) 
# [[1, 2, 3], [1, 2, 3]]
# [[1, 2, 3], [1, 2, 3]]

# [['a', 2, 3], ['a', 2, 3]]
# [[1, 2, 3], ['a', 2, 3]]
# 拷贝可变对象，修改值是对象引用的操作，循环可生成不同的对象

# 8
class A(object):
    def foo(self):
        print('class A')
    
class B(object):
    def foo(self):
        print('class B')

class C(A, B):
    pass
print(C().foo())
# C继承了A,B 有结果即返回
print('------------------------------')
class A(object):
    def foo(self):
        print('class A')

class B(A):
    def foo(self):
        pass

class C(A):
    def foo(self):
        print('class C')

class D(B, C):
    pass
print(D().foo())
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 9
lst1 = list(range(30))
print('ID:', id(lst1))

lst1 += [1]
print('ID(+=):', id(lst1))

lst1 = lst1 + [2]
print('ID:',id(lst1))

lst2 = []
print(id(lst2))

lst2.append(1)
print(id(lst2))

lst2.extend([1])
print(id(lst2))

# 10
import datetime

print('"daetime.time(0,0,0)"(midnight) ->', bool(datetime.time(0,0,0)))
print('"datetime.time(1,0,0)" (1 am) ->', bool(datetime.time(1,0,0)))

# 11
a = float('main')
print('a is a', a is a)

a = 1
b = 1
print(a is b)

c = -9
d = -9
print(bool(c is d))

a = 'Hello world'
b = 'Hello world'
print(a is b)
print(a == b)

a = float('1.22')
print(a is a)
print(a == a)
# is判断ID，==比较值； 小整数对象[-5, 256] 


# 12 
from copy import copy, deepcopy
from pickle import dumps, loads

a = ['x','y','z']
b = [a] * 3
c = copy(b)
d = deepcopy(b)
e = loads(dumps(b, 2))

b[1].append(999)
b.append(888)
c[1].append(999)
c.append(777)
d[1].append(999)
d.append(222)
e[1].append(999)
e.append(111)

print(a)
print(b)
print(c)
print(d)
print(e)

# ['x', 'y', 'z', 999, 999]
# [['x', 'y', 'z', 999, 999], ['x', 'y', 'z', 999, 999], ['x', 'y', 'z', 999, 999], 888]
# [['x', 'y', 'z', 999, 999], ['x', 'y', 'z', 999, 999], ['x', 'y', 'z', 999, 999], 777]
# [['x', 'y', 'z', 999], ['x', 'y', 'z', 999], ['x', 'y', 'z', 999], 222]
# [['x', 'y', 'z', 999], ['x', 'y', 'z', 999], ['x', 'y', 'z', 999], 111]
# a 列表赋值给 b，b[1].append(999),此时a = ['x', 'y', 'z', 999] 
# b 又被 c浅拷贝，最终 a = ['x', 'y', 'z', 999, 999]
# b[1] 中三个子列表指向同一个内存地址，即对 a 的引用


# 13
l1 = ['a','b','c']
l2 = list(range(10))
# print(l1+l2)
#  + 合并列表资源浪费，会重新创建一个列表，复制完成合并
l3 = [77,88]
l4 = l3.extend(l2)
print(l3)
# 数据类型相同，推荐使用extend()函数

l5 = ['a','hh345','gg12','ff123','vv4444','nn33333']
print(l5.sort(key=lambda x: x[0], reverse=True))
l6 = [i for i in range(10)]
print(l6[:5:2])
print(l6[::-1])

l7 = ['zhang','wang','lee']
ma = dict((v,i) for i, v in enumerate(l7))
print(ma)
# enumerate 函数返回（index，value）元祖

l8 = sorted(['r','e','d','f'])
l9 = sorted('hello python')
print(set(l9))
# sorted和set合用，生成唯一元素有序列表

seq1 = ['zhang','wang','lee']
seq2 = ['san','si','wu']
for i, (a,b) in enumerate(zip(seq1, seq2)):
    print('%d: %s %s' % (i, a, b))
#  enumerate和zip 函数合用，压缩序列

seq3 = [('a','b'),
        ('c','d'),
        (111, 22)]
m, n = zip(*seq3)
print(m,n)
#  列元素转为行，行元素转为列


# 14
dict1 = {'k': 'abc', 'v':'123'}
dict2 = {v : k for k, v in dict1.items()}
print(dict2)
# K-V 互换
dict3 = {'a':12,'b':22,'c':22,'d':14,'e':6,'f':77}
dict4 = sorted(dict3.items(), key=lambda item: -item[1])
print(dict4)
# 字典值降序输出
dict5 = sorted(zip(dict3.values(), dict3.keys()))
print(dict5)
# zip() 函数会对第一个元素进行排序

# 15
def func(n):
    for i in range(n):
        yield call(i)
        print('i=', i)
    print('this is a test...')

def call(i):
    return i*2
for i in func(5):
    print(i, ',')


# 16
def func():
    try:
        print('one:')
    except IndexError:
        print('rasised IndexError')
    else:
        print('No error in try-block')
func()

for i in range(5):
    print(i)
else:
    print('compleled for-loop')
for i in range(2):
    print(i)
    i += 1
    break
else:
    print('completed for-loop')

# 17
class Fib:
    ''' 迭代器实现斐波那契数列 '''
    def __init__(self, max_vlaue):
        self.prev = 0
        self.curr = 1
        self.max_value = max_vlaue
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr <= self.max_value:
            res = self.curr
            self.prev, self.curr = self.curr, self.prev + self.curr
            return res
        else:
            raise StopIteration()
print(Fib(5))    

def fib(max_value):
    ''' 生成器实现斐波那契数列 '''
    prev, curr = 0, 1
    while curr <= max_value:
        yield curr
        prev, curr = curr, prev + curr
fib(5)            

def deco(func):
    ''' 最简单装饰器 '''
    def wra(*args, **kwaegs):
        return func()
    return wra


import datetime

def count_time(func):
    ''' 函数运行时间 '''
    def wra(*args, **kwargs):
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        total_time = (end_time - start_time).total_seconds()
        print('time is %s seconds' % total_time)
    return wra

@count_time
def main():
    print('>>>Time is start : ')
    for i in range(10):
        for j in range(i):
            print(j)

if __name__ == '__main__':            
    main()
    

import time

class Retry(object):
    ''' 最大连接次数 '''
    def __init__(self, max_retries=3, wait=0, exceptions=(Exception, )):
        self.max_retries = max_retries
        self.exceptions = exceptions
        self.wait = wait

    def __call__(self, func):
        def wrap(*args, **kwaegs):
            for i in range(self.max_retries + 1):
                try:
                    res = func(*args, **kwaegs)
                except self.exceptions:
                    time.sleep(self.wait)
                    continue
                else:
                    return res
        return wrap


# 18
class Method(object):
    x = 666
    
    def __init__(self):
        self.y = 777
    
    def bar1(self):
        print('a method')

    @classmethod
    def bar2(cls):
        print('a classmethod')
    
    @staticmethod
    def bar3():
        print('a staticmethod')

    def func1(self):
        print(self.x)
        print(self.y)
        self.bar1()
        self.bar2()
        self.bar3()
    
    @classmethod
    def func2(cls):
        print(cls.x)
        print(cls.y)
        cls.func1()
        cls.func2()
        cls.func3()
    
    @staticmethod
    def func3(obj):
        print(obj.x)
        print(obj.y)
        obj.func1()
        obj.func2()
        obj.func3()

m = Method()
m.func1()
m.func2()
m.func3()


#  19
class User:
    ''' 属性监听 '''
    #q = [i for i in range(10000)]
    q = [1,2,3]
    def __init__(self):
        self.money = 100000
        self.name = 'lee'
    
    def __setattr__(self, name, value):
        if name == 'money' and value < 0:
            raise ValueError('money < 0')
        print('set %s to %s' % (name, value))
        object.__setattr__(self, name, value)
    
    def __getattribute__(self, name):
        print('get %s ' % name)
        return object.__getattribute__(self, name)
        
    def func(x, y):
        return x ** y

a = User()
print(User.__dict__)
print(a.__dict__)


# 20
from functools import wraps
import time
import threading

def deco(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrap

@deco
def foo(x, y):
    t = 0
    while t < 10:
        t += 1
        print('x:{}, y:{}'.format(x, y))
        time.sleep(2)
foo(666, 999)
