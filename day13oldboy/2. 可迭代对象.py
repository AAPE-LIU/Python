'''可以被for循环的对象就可以被称为是可迭代对象'''
class Foo(object):
    pass
obj = Foo()

'''如何让一个对象变成可迭代对象？'''
'''在类中实现__iter__方法且返回一个迭代器（生成器）'''
class Fooo(object):
    def __iter__(self):
        return iter([1,4,5,6,7])
obj2 = Fooo()
val = obj2.__iter__()
print(type(val))

'''=====================也可以通过下面这种方法==================='''
class Fooo(object):
    def __iter__(self):
        v = [1,4,5,6,7]
        return v.__iter__()
obj2 = Fooo()
val = obj2.__iter__()
print(type(val))

'''============= =另外，由于生成器是一种给特殊的迭代器，因此返回一个生成器也是可以的============'''
class Fooo(object):
    def __iter__(self):
        yield 1
        yield 3
        yield 6
        yield 10
obj2 = Fooo()
val = obj2.__iter__()
print(type(val))