'''
python中的约束没有java或者C#那么严格，在python中即使类中没有那个方法也不会报错
但是Java或者C#不一样，如果约束中有该方法，那么你继承了约束类，就必须要有这个方法，否则就报错
'''
# 约束类的格式
class Interface(object):
    def send(self):
        raise NotImplementedError
# 以上就是约束的具体格式
# 含义就是，谁继承了我，谁就要有我这里面定义的所有方法
# 在Java中没有会报错。在python中并不会报错，但是如果调用失败会报错
# 这就相当于把类给约束住，你必须要有该方法
class Foo(Interface):
    def send(self):
        print('发送短信')
class Email(Interface):
    def send(self):
        print('发送邮件')
class QQ(Interface):
    pass

obj = Email()
obj.send()

obj = QQ()
obj.send()