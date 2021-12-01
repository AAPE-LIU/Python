'''
os.path.exists(path) 如果path存在，返回True，如果path不存在，返回False
os.stat(path).st_size 获取文件大小
os.path.abspath()  获取当前工作路径与文件名的拼接路径
os.path.dirname()  就是查找当前文件的上一级目录，即当前文件存放在哪个文件夹里所以是dirname
os.path.join()  做路径的拼接，会自动拼接成合适的格式
os.listdir()  列出一个文件夹下所有的文件
os.walk()  深度遍历目标文件夹下的所有文件
'''
import os
path = '第八章复习参考题.doc'
print(os.path.abspath(path))
# 打印出文件的绝对路径，其实就是将此代码所在的文件夹和path拼接起来
# 不管文件在不在此代码所在的文件夹中，都会进行拼接


# 就是查找当前文件的上一级目录，即当前文件存放在哪个文件夹里所以是dirname
path2 = r'C:/Users/prominent/Desktop/老男孩python/day5/os模块.py'
print(os.path.dirname(path2))  # C:/Users/prominent/Desktop/老男孩python/day5


v = 'abc.txt'
path2 = r'C:\Users\prominent\Desktop\老男孩python\day5'
abspath = os.path.join(path2,v)
print(abspath)


file = os.listdir(r'C:\Users\prominent\Desktop\老男孩python\day5')
print(file)

result = os.walk(r'C:\Users\prominent\Desktop\老男孩python\day5')
print(result)  # <generator object _walk at 0x000001CBA14B4510>
# 生成器：相当于我现在还不给你找，等你遍历我的时候，我再给你找，生成器只能迭代一次
# for i in result:
#     print(len(i),end=' ')
    # 3 3 3 3
    # 这里的3代表什么意思呢？意思将分成3个等级，一级是正在查看的目录
    # 第二级是正在查看的目录中的文件夹，第三级是正在查看的目录中的所有非文件夹类型文件
print('========================================')
'''
打印出文件夹中所有的文件，不管有几层目录
'''
for a,b,c in result:
    # print(a,111,b,111,c)
    for item in c:
        abspath = os.path.join(a,item)
        print(abspath)
