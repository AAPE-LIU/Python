import studen  # 这里是可以import的，因为运行这个程序，当前文件所在的目录就会被加载到sys.path中去
import x  # 但是x并不属于bin目录下的东西，为什么可以import呢？因为pycharm默认会将整个工程导入进去
import os
import sys
x.func()
# 但是在cmd中并不会导入进去，如果想让整个程序导入进去，我们还得做一些工作，就是将整个目录导入进去
# 但是又不能直接写一个绝对路径，因为这样的话，如果别人用这个代码，路径不一样就会报错
# 因此可以用一段代码来获取上级目录
print(__file__)
path1 = os.path.dirname(os.path.abspath(__file__))
path2 = os.path.dirname(path1)
sys.path.append(path2)
print(path2)
