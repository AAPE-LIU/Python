# 类可不可以相加呢？
a = 12
b = 13
c = a + b
print(c)
a = 'skjdhf'
b = 'asijdh'
print(a+b)

class Foo(object):
    def __add__(self, other):
        return 123

obj1 = Foo()
obj2 = Foo()
val = obj1 + obj2  # __add__是由obj1触发的，因此会到obj1中执行__add__
# 因此self的值就是obj1，而other的值是obj2
print(val,type(val))  # 123 <class 'int'>