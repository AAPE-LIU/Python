'''
python2中的类分为 经典类 和 新式类
python3中只有新式类，因为所有的类默认都会继承object类
'''
# 如果在python2中这样定义，则称为经典类：
class Foo:  # 不会默认继承object类
    pass

# 如果在python2中这样定义，则称为新式类
class Fooo(object):
    pass

# 在python3中两种写法是一样的，因为所有的类默认都是会继承object类的，全部都是新式类
# 新式类是一种先进的写法，因此为了统一python2，python3都为新式类，我们统一加上object
class Foooo(object):
    pass

