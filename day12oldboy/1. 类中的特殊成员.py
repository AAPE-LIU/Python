'''
__init__() : 初始化方法
__new__()：创建对象方法。 其实在我们实例化一个对象的时候，是分为两个步骤的。
        1：创建一个空的对象obj
        2：执行__init()，给对象中进行赋值（初始化）
        而__new__的作用就是创建这个空的对象
        平时写类的时候也并没有使用__new__方法那么空对象是怎么创建的呢？因为默认会使用object中的
        __new__方法，因此我们不需要手动写__new__
__call__()：对象后面加括号执行call方法
__getitem__:特定的格式触发
__setitem__:
__delitem__:
__str__:当你实例化了一个对象之后，你要去打印这个对象，__str__是什么你打印出来就是什么，不要太相信
        python中打印出来的东西，打印出来的看着是字符串，他可能并不是字符串，就比如说你打印对象，如果
        __str__中return的是一个字符串，你打印出来就是一个字符串，但是他其实打印的是一个对象
__dict__:自动找到类中所有的值，并将它们转换为字典形式
'''

class Foo(object):
    def __setitem__(self, key, value):
        print(key,value)

    def __getitem__(self, item):
        print(item + 'uuu')

    def __delitem__(self, key):
        print(key + 'ttt')

    def __str__(self):
        return 'kjsahdgiujoasdjflab'

obj = Foo()
obj['name'] = '刘总'  # name 刘总  只要出现了这种写法就对应于类中的__setitem__
val = obj['age']  # ageuuu  只要出现了这种写法，就对应于类中的__getitem__方法
del obj['class']  # classttt  只要出现了这种写法，就对应于类中的__delitem__方法
# 并且参数都是一一对应的，按照前后位置一一对应

obj2 = Foo()
print(obj2)  # kjsahdgiujoasdjflab
print(obj2,type(obj2))  # kjsahdgiujoasdjflab <class '__main__.Foo'>
                        # 以后不要相信打印出来的东西，一定要type一下，看看他到底是个什么东西

'''=============================__dict__==========================='''
class Fooo(object):
    def __init__(self,name,age,email,gender):
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender

obj2 = Fooo('刘总',22,'1369578672@qq.com','male')
val = obj2.__dict__
print(val)
