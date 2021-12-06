'''
绑定方法是定义在类中的，绑定方法的使用需要先将类实例化成一个对象
然后通过对象来调用该方法
'''

'''
静态方法也是定义在类中的，但是要由一个python内部定义的静态装饰器来装饰一下
静态方法可以直接通过类名来调用，不需要实例化出来一个对象
'''
# 下面这种写法很浪费资源，因为实例化出来的这个对象，并没有什么用，就是一个空的对象
class Base:
    def func1(self,a,b):
        print(a,b)

obj = Base()
obj.func1(13,24)

# 什么样的才不是浪费资源呢？才不是空的对象呢？比如下面这种
class Base2:
    def __init__(self,name):
        self.name = name
    def func2(self,a,b):
        print(self.name,a,b)

obj = Base2('刘总')
obj.func2(13,24)
# Base2.func2(12,34,16)  如果不是静态方法的话，直接由类调用方法，会报错，没办法调用

# 那对于浪费资源的那种该怎么做呢？将他转换为静态方法，不需要实例化出来对象就可以
# 注意，因为静态方法并不需要实例化对象所以静态方法中自然也就没有self参数
class Base3:
    @staticmethod
    def func1(a,b):
        print(a,b)

Base3.func1(10,20)
obj = Base3()
obj.func1(10,50)  # 通过对象也可以使用静态方法，但是不到万不得已不要这样用，不推荐
