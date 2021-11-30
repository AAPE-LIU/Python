'''
装饰器：在不改变原函数内部代码的基础上，在函数执行之前和之后自动执行某个功能
'''
def func (args):
    def inner():
        print('我是修饰befor')
        v = args()  # 这个就相当于执行了下面的index函数，因此在执行inner的过程中可以在这段代码
                    # 前后加上一些代码，用来作为执行index的修饰
        print('我是修饰after')
        return v
    return inner

def index():
    print('123')
    return 666

index = func(index)
# index()
print(index())

# 但是上面的代码那样写，很繁琐，所以在python中有专门的语法用来使用装饰器
# @起装饰作用的函数
def func2(args):
    def inner():
        print('我是修饰befor')
        v = args()
        print('我是修饰after')
        return v
    return inner

# 第一步：执行func函数并将下面的函数参数传递，相当于func2(index2)
# 第二步：将func的返回值重新赋值给下面的函数名，即index2 = func2(index2)
@func2

def index2():
    print('123')
    return 666
print(index2())

'''
装饰器的应用场景
如果有多个需要计算同样操作的函数，用装饰器就可以大量节省代码量
'''
import time
def decorate(args):
    def inner():
        begin_Time = time.time()
        f = args()
        end_Time = time.time()
        print('程序运行的时间为{}'.format(end_Time-begin_Time))
        return f
    return inner

@decorate
def itera():
    time.sleep(2)
    for i in range(10000):
        i = i + 1
    return i

@decorate
def xy():
    time.sleep(2)
    print('234')
    return 333

@decorate
def yz():
    time.sleep(2)
    print('789')
    return 456

itera()
xy()
yz()