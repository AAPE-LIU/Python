'''
根据对象的继承关系，挨个去找，要搞清楚对象是谁创建的，就从谁那里继承下去
'''

class Foo(object):
    def func(self):
        print('Foo.func')

class Child(Foo):
    def func(self):
        print('Child.func')

obj = Child()
obj.func()  # 会优先去自己的类中去找有没有func方法，但是如果我就是想执行Foo中的func方法该怎么做呢？
print('=======================================================')
'''============================================================'''
class Foo(object):
    def func(self):
        print('Foo.func')
        return 123

class Child(Foo):
    def func(self):
        v = super().func()
        print('Child.func',v)

obj = Child()
obj.func()

'''==================如果直接的父类中没有要执行的方法该怎么办呢？=============================='''
# 没关系，super支持按照继承关系去查找，并不局限于直接父类
print('=======================================================')
class Base(object):
    def func(self):
        print('Base.func')
        return 123
class Foo(Base):
    pass
class Child(Foo):
    def func(self):
        v = super().func()
        print('Child.func',v)

obj = Child()
obj.func()

'''================================如果是下面这种多继承关系，该怎么办呢============================='''
print('=======================================================')
class Base1(object):
    def func(self):
        super().func()
        print('Base1.func')
class Base2(object):
    def func(self):
        print('Base2.func')
class Foo(Base1,Base2):  # Foo -> Base1 -> Base2  遇到super会按照这个继承关系找下去，因为对象是Foo创建的
                            # 因此继承关系就按照Foo中的继承关系来
    pass
obj = Foo()
obj.func()
