'''
递归限制次数1000，系统规定的，python解释器规定的
'''
import sysPart
limit = sysPart.getrecursionlimit()
print(limit)  # 1000
# 也可以通过sys.setrecursionlimit()来修改限制次数，但是最好不要修改，你只需要知道就可以

