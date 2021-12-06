'''
python中的self参数，在类中的每个方法中都要有，而且要放在第一个
并且这个self参数并不一定是非要叫作self，它叫做任何东西都可以，
只不过大家都叫self，因此我们也一定要将他写作self，这样显得专业
它代表的含义就是：在使用类中的方法时要先将类实例化为一个对象，
而这个对象叫做什么名字，这个self就是什么
'''

'''
在类中如果有一个方法叫做__init__(self)那么就代表这是一个初始化方法
类实例化的时候，这个方法会自动执行，而其他方法，都要调用的时候才会执行
这个方法里面可以传参数，并且可以将这些参数封装到这个类中
'''

class Base:
    x = 1

obj = Base()  # 创建的时候是一个空的对象，里面可能就只有一个类指针
print(obj.x)  # 这里是可以用实例化出来的对象来取到类中的变量的
obj.y = 123  # 在对象中创建一个值为123的变量y
print(obj.y)
obj.x = 456  # 在对象中创建一个值为456的变量x，并不能修改类中的成员变量x
print('这是obj.x:',obj.x)
print('这是Base.x:',Base.x)

'''==========================================================='''
class Base1:
    x = 1

class Foo(Base1):
    pass

print(Base1.x)
print(Foo.x)
Base1.x = 666
print(Base1.x)
print(Foo.x)
Foo.x = 999  # 对于继承的也是一样，子类修改变量名，只能修改自己的，并不能修改父类的，
# 就好像老子有多少钱并不是儿子说了算的，老子自己说了才算数
print(Base1.x)
print(Foo.x)

'''======================================================'''
class Parent:
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass
class Child3(Child2):
    pass
print(Parent.x,Child1.x,Child2.x)  # 1 1 1
Child1.x = 22
print(Parent.x,Child1.x,Child2.x)  # 1 22 1
Child2.x = 323
print(Parent.x,Child1.x,Child2.x)  # 1 22 323
print(Parent.x,Child1.x,Child2.x,Child3.x)  # 1 22 323 323
