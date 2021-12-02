'''
在python2中每一个文件夹中都必须包含一个__init__.py文件，这相当于声明这个包
在python3中不必这么做，但是如果想让别人使用我们在包中创建的方法，最好使用package
如果只是搞一个文件夹就没必要在添加一个__init__.py文件了
'''
import sys
print(sys.path)