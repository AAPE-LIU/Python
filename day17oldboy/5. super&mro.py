'''
super永远不是找父类，而是找mro顺序中的下一个类
'''
class A:
    def func(self):
        print('in a')

class B(A):
    def func(self):
        print('in b')
        super().func()

class C(A):
    def func(self):
        print('in c')
        super().func()

class D(B,C):
    def func(self):
        print('in d')
        super().func()
d = D()
d.func()
print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]