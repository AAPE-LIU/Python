'''
如果我想用liuzong包下面的jd下面的f2（）该怎么做？
'''
# 按照之前的内容，可能会这样做
import liuzong.jd as f  # 注意，import的时候最低最低也是导入py级别，不能再低一级导入函数
f.f2()

'''方法2'''
from liuzong import jd
jd.f2()