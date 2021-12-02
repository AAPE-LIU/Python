def f1():
    print('淘宝')
import jd  # 这里为什么可以导入？因为执行这个文件的时候，会将这个文件所在的文件夹的目录
# 放入导sys.path中，因此可以导入
jd.f2()
# episode 176