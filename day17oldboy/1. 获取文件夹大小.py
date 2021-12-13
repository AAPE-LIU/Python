'''获取整个文件夹大小的时候能够直接os.path.getsize()整个文件夹路径么？
答：不可以，因为这种方法只能让我们获得这个文件夹创建的时候内置的一些属性大小
比如，这个文件夹创建的时候开辟了4K空间用来存储内部文件的一些信息，比如创建日期，权限等等
这些内存并不包含其内部的文件的大小
'''
import os
def file_size(path):
    size = os.path.getsize(path)  # 4096
    print(size)
    abspath = os.walk(path)
    print(abspath)  # <generator object _walk at 0x000001746B7777B0>
    sum_count = 0
    for base_path,dir_path,file_path in abspath:
        for file_name in file_path:  # 对base_path中的文件进行遍历
            file = os.path.join(base_path,file_name)  # 进行文件的拼接
            sum_count += os.path.getsize(file)
    return sum_count

size = file_size(r'C:\Users\prominent\Desktop\老男孩python')
print(size)