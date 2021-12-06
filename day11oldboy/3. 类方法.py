'''
类方法和静态方法本质上是一样的，只不过类方法多传了一个参数cls(class的缩写)
cls中存储的是当前类的类名
类方法也需要由类直接调用，不需要实例化对象,类方法要由classmethod装饰器来装饰
类方法依然推荐用类名调用，不推荐用对象调用，其实用对象调用也可以，但是最好别用
'''
class Base2:
    def __init__(self,name):
        self.name = name
    def func2(self,a,b):
        print(self.name,a,b)

    @staticmethod
    def func1(a,b):
        print(a,b)

    @classmethod
    def func3(cls,a,b):
        print('cls是当前的类：',cls)  # cls是当前的类： <class '__main__.Base2'>
        print(a,b)  # 15 29
Base2.func3(15,29)