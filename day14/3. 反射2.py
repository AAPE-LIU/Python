'''python中一切皆对象: py文件，包，类，对象'''
'''如果有一个py文件，可以把它看作是一个模块，这里就以 x.py 模块举例'''
import x
print(x.NUM)

func1 = getattr(x,'NUM')
print(func1)

func2 = getattr(x,'Foo')
print(func2)  # <class 'x.Foo'>

obj = func2()
print(obj)  # <x.Foo object at 0x0000018F2DA8DCD0>

obj.name = 'kjdflkg'
obj.funcc1('dhjfgkjhdsf') # 不能直接拿func2来获取，因为funcc1是绑定方法，绑定方法只能拿对象来获取

func2.name = '123456'
func3 = getattr(func2,'name')  # 在'x.Foo'中定义一个name，可以直接取到
print(func3)

delattr(func2,'name')

# func3 = getattr(func2,'name')  # 删掉之后就取不到了
# print(func3)

# func3 = getattr(func2,'name')  #  type object 'Foo' has no attribute 'name'类中的绑定方法中的name也不可以直接获取到
# 要先实例化出来该类的对象，才可以

obj2 = func2()
obj2.funcc1('我是实例化出来的obj2的name')
# name = getattr(func2,'name')  # type object 'Foo' has no attribute 'name'
name = getattr(obj2,'name')