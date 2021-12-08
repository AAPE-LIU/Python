'''
__enter__:
__exit__:
'''
class Foo(object):
    def __enter__(self):
        print('123')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(456)

obj = Foo()
with obj:  # 在执行这一句with的时候会将__enter__执行，然后再去执行下面缩进里面的内容，
    # 退出缩进的时候会执行__exit__的内容
    print(111)

'''======================================================'''
class Foo2(object):
    def __enter__(self):
        self.ff = open('a.txt',mode='w',encoding='utf-8')  # mode='a'的时候会从文本末尾开始写，mode='w'会将文本清空从头开始写
        return self.ff
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ff.close()

obj = Foo2()
with obj as ff:  # 在执行这一句with的时候会将__enter__执行,ff用来接收__enter__的返回值
    ff.write('刘总长得帅\n')  # 执行完__enter__之后，会执行缩进里的内容，
    ff.write('刘总长得壮\n')  # 然后缩进内容执行完之后，会执行__exit__里面的内容
    ff.write('刘总长得高\n')
    ff.write('刘总很有钱\n')
    ff.write('刘总很有才\n')
    ff.write('刘总很友善')
# 一旦遇到  with 对象  这种写法就先把这两个方法写上，一定会用到这两种方法，因为不写的话，不支持  with 对象
