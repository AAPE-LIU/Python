'''
我想让用户使用的时候，先打印一个已登录，或者扩展一些的话就是判断是否登陆了
如果登陆了，就可以调用，否则不能调用
'''
def admin(args):
    def inner():
        print('已登录')
        args()
    return inner

@admin
def func1():
    print('func1')

@admin
def func2():
    print('func2')

@admin
def func3():
    print('func3')
