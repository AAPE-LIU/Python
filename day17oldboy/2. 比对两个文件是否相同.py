'''
比对两个文件是否相同可以用md5加密来进行比对
同一个文件的多次md5update得到的数值是相同的
'''
import os
import hashlib
path1 = r'E:\机器学习进阶\机器学习进阶\1.课时001： mlcamp_course_info(Av289932147,P1).mp4'
path2 = r'E:\机器学习进阶\机器学习进阶\contrast.mp4'
def md5_issame(path):
    md5 = hashlib.md5()  # 实例化一个md5对象
    size = os.path.getsize(path)  # 先得到文件的大小，用来做终止循环的条件
    with open(path,mode='rb') as f:
        while size > 1024:  # 当文件中还剩余超过一次的读取量的时候，就继续循环，当小于一次的读取量的时候，就跳出循环
            content = f.read(1024)  # 读取1024个字节的文件
            md5.update(content)  # 对读取到的文件进行加密
            size -= 1024  # 改变剩余的未读取的文件内容
        else:
            content = f.read(size)
            md5.update(content)
            size = 0
    return md5.hexdigest()
print(md5_issame(path1) == md5_issame(path2))

