'''设计模式很重要，是代码拔高的关键'''
# 多例，每实例化一次就创建一个新的对象
class Foo(object):
    pass
obj1 = Foo()  # 实例，对象
obj2 = Foo()  # 实例，对象
print(obj1,obj2)  # 0x00000286D031DC40>  0x00000286D031DCD0  地址不一样

# 单例，无论实例化多少次，都用第一次创建的那个对象
'''Singleton是单例的标准类名'''
v1 = Foo()
v2 = Foo()
# 想办法让v1和v2的地址相同
'''创建对象的时候调用的是new方法，new方法的返回值就是那个创建的空对象'''
instanc = None
class Foo(object):
    def __new__(cls, *args, **kwargs):
        global instanc
        if instanc:
            return instanc
        instanc = object.__new__(cls)
        return instanc

v1 = Foo()
v2 = Foo()
print(v1,v2)  # 0x00000166EE707A30  0x00000166EE707A30  地址一样


class Foo(object):
    instanc = None
    def __new__(cls, *args, **kwargs):
        if not Foo.instanc:
            Foo.instanc = object.__new__(cls)
        return Foo.instanc

class Foo(object):
    instanc = None
    def __new__(cls, *args, **kwargs):
        if not cls.instanc:
            cls.instanc = object.__new__(cls)
        return cls.instanc
# 本质上的单例模式是这样的，最终版的还要加锁，是为了支持多线程
# 无论你实例化多少次，永远用的都是第一次创建的那个对象，开辟的那块空间
