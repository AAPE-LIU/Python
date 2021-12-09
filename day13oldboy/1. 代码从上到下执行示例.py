'''执行下面这段代码，会打印Foo方法中的“你好啊刘总”么？'''
class Foo:
    print('你好啊刘总')
    def func(self):
        pass
'''答案是会的，因为python中从上到下执行代码的时候，会将类中的代码执行，但是类中的方法内部的
代码不会立即执行，会在调用的时候才执行'''

'''
类里面还会嵌套类，这样是可行的
类中嵌套的类，在运行代码的时候，内部的print也会执行，但是函数内部的不会执行
'''
class Meta:
    print('好家伙')
    class Inner:
        print('你小子')
        def func(self):
            print('你看我执不执行就完了')

'''!!!!!!!!!!!!!!!!!!!!!!!!超级易错点！！！！！！！！！！！！！！！'''
class Fooo(object):
    def __init__(self,age):
        self.age = age

    def func(self):
        print(self.age)
data_list = [Fooo(8),Fooo(10)]
for item in data_list:
    print(item.age,item.func())  # 8
                                # 8 None
                                # 10
                                # 10 None

'''===========================源码中经常出现，看懂它！====================='''
class Base(object):
    def __init__(self,name):
        self.name = name

class Foo1(Base):
    def __init__(self,name):
        super().__init__(name)
        self.name = "老大爷"
obj1 = Foo1('alex')
print(obj1.name)

obj2 = Base('alex')
print(obj2.name)