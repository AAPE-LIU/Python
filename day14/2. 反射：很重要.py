'''根据字符串的形式去某个对象中操作它的成员'''
'''
getattr(对象，'字符串')：根据字符串的形式去某个对象中获取对象的成员
        getattr(对象，'字符串'，返回值)：如果找到了该字符串方法，则返回该字符串方法，如果没找到就返回第三个参数，返回值
hasattr(对象，'字符串')：根据字符串的形式判断某个个对象中是否有该对象的成员
setattr(对象，变量，值)：根据字符串的形式去改变或者设置某个对象中成员变量的值.注意！！这个是针对变量的
delattr(对象，变量)：根据字符串的形式去删除某个对象中成员变量的值
'''
class Foo(object):
    def __init__(self,name):
        self.name = name
obj = Foo('liuzong')
print(getattr(obj,'name'))
print(obj.name)

'''========================================================'''
class Fooo(object):
    def func(self,name):
        print('func')
        self.name = name

obj2 = Fooo()
fun = getattr(obj2,'func')
fun('刘大头')
print(hasattr(obj2,'func'))
print(getattr(obj2,'name'))

setattr(obj2,'name','刘小头')
print(getattr(obj2,'name'))
print(obj2.name)


class Foooo(object):
    pass

obj3 = Foooo()
setattr(obj3,'age',30)
print(obj3.age)
'''==================================================='''
class Base(object):
    pass
obj4 = Base()
obj4.name = 'ksjhdf'
print(getattr(obj4,'name'))  # ksjhdf
delattr(obj4,'name')
print(getattr(obj4,'name'))  # AttributeError: 'Base' object has no attribute 'name'