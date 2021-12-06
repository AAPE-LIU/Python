'''
1.类
    类变量
    绑定方法
    静态方法
    类方法
    属性
2.实例
    实例变量
'''

'''
成员修饰符：
    共有
    私有：类的内部才访问的到，外部访问不到
'''
# 下面这种情况可以访问到，但是如果改变成私有变量呢？
class Foo:
    def __init__(self,name):
        self.name = name

    def func(self):
        print(self.name)

obj = Foo('刘总')
print(obj.name)

'''=============================私有成员变量=================================='''
'''写法：在变量名前面加上__'''
class Foo:
    def __init__(self,name):
        self.__name = name

    def func(self):
        print(self.__name)

obj = Foo('刘总')
# print(obj.name)  # 'Foo' object has no attribute 'name'
# 上面这个访问不到私有成员变量，那么该怎么样访问到呢？
# 用类内部的方法去访问
obj.func()  # 刘总
# print(Foo.name)  # 只有类变量，类方法才可以被类直接调用，这种从成员方法，成员变量都比可以被类直接调用

'''不可访问私有变量'''
class Fooo:
    __x = 3
    def func(self):
        print(self.__x)
# Fooo.__x  # type object 'Fooo' has no attribute '__x'  访问失败
obj = Fooo()
obj.func()  # 3

'''=============================私有方法============================='''
class Fooo:
    __x = 3
    def __func(self):
        print(self.__x)
    def show(self):
        print('show')
        self.__func()
# Fooo.__x  # type object 'Fooo' has no attribute '__x'  访问失败
obj = Fooo()
# obj.func()  # 访问不到
obj.show()  # 通过show访问到私有方法__func，然后私有方法__func访问到私有类变量__x


# 私有变量甚至私有方法，即使是自己的子类也无法访问
class Father:
    def __func2(self):
        print('我是你爸爸')
class Fooo(Father):
    __x = 3
    def __func(self):
        print(self.__x)
    def show(self):
        print('show')
        self.__func()
obj = Fooo()
# obj.__func2()  # 访问不到
obj._Father__func2()  # 我是你爸爸
'''这个为什么可以访问到呢？通过强制访问私有变量的方法实现的'''
'''强制访问格式：_类名__私有类名方法或者私有类变量'''
