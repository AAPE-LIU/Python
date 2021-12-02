'''
sys.argv()
sys.path  他其实是一个列表，告诉python导入包的时候去哪个目录下面找
        平时所用的内置模块，自定义模块，外部模块所存放的位置是不同的，python哪知道
        去哪里找，因此有了sys.path这个列表，这里面是所有存放包的路径
        如果你自己写了一个模块，不在sys.path中，而你又想导入，可以将你写的哪个模块的路径
        用append添加到sys.path中去
sys是解释器相关的数据：递归次数/引用次数
'''
import hashlib
import sys
print(sys.argv)
print(sys.path)
for path in sys.path:
    print(path)