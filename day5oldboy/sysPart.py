# sys.getrecursionlimit() 得到最大递归层次数
# sys.getrefcount()  获取文件大小
# sys.stdout.write -> print  等价于print()
# sys.argv  获取用户执行脚本时传入的参数
# sys.exit(0/1)  括号内是0表示正常结束，不是0表示异常结束
# shutil.rmtree(path)
#
'''
以下代码在cmd窗口执行
D:\Python\python.exe C:/Users/prominent/Desktop/老男孩python/day5/sysPart.py
复制上面这条命令，执行
如果在这条命令后面加上 空格 然后再加路径名，argv就会将他自动记录到列表中去，然后可以用
shutil.rmtree(路径名)用来删除路径所对应的文件夹
'''
import shutil
import sys
path = sys.argv[2]
print('打印删除path')
shutil.rmtree(path)