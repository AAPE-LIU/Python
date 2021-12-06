class Foo:
    def func1(self):
        print(123)
        return 666
obj = Foo()
result = obj.func1()  # 调用这个方法的时候，要在方法名后面加括号，代表执行
print(result)

'''那么什么是属性呢？属性该怎么定义呢？'''
'''属性要用@property装饰器来定义，并且只有一个参数self，
定义了之后，再调用这个属性，就不需要加括号了，直接 . 就可以执行'''
class Foo:
    @property
    def func1(self):
        print(123)
        return 666
obj = Foo()
result = obj.func1  # 调用这个属性的时候，直接 . 就可以，不需要加（）
print(result)