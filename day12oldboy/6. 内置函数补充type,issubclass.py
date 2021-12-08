'''=============================type========================='''
class Fls(object):
    pass
class Foo(Fls):
    pass
obj = Foo()
if type(obj) == Foo:
    print(True)

'''=============================issubclass(A,B)========================='''
# 判断A是不是B的派生类，不一定非得是直接派生类，隔了好几层也可以，只要他可以找得到
class Pig(Foo):
    pass
print(issubclass(Pig,Foo))  # True

'''=============================isinstance(A,B)========================='''
# 判断对象是不是父类或其基类的实例，即使是他的直接类的父类，爷爷类，祖爷爷类，也会判断成True
'''这个和type不同，type只会是他的直接父类才返回True'''
obj = Pig()
print(isinstance(obj,Pig))  # True
print(isinstance(obj,Foo))  # True
print(isinstance(obj,Fls))  # True
