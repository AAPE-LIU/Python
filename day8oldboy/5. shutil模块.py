import shutil
'''
1. 删除文件夹
shutil.rmtree(要删除的文件夹)

2. 移动文件，将A文件移动到B文件，如果A，B本来就再一个文件夹中，那么它的功能就是重命名
shutil.move(A, B)

3. 压缩文件
shutil.make_archive(压缩之后的文件，要压缩成的类型，要压缩的文件)

4. 解压文件
shutil.unpack_archive(要解压的压缩包，extract_dir=解压到哪里去，要解压的文件的类型)
解压的时候可以自动帮你创建目录

'''
# 实现这样一个功能：
'''
1.压缩liuzong文件夹
2. 将压缩包放到code目录下，默认不存在
3.将文件解压到E:\\x1目录中
'''
import shutil
import os
if not os.path.exists('code'):
    os.mkdir('code')
shutil.make_archive(os.path.join('code','liuliuqiu'),'zip','liuzong')
# shutil.move('liuliuqiu.zip','./code')
filepath = os.path.join('code','liuliuqiu') + '.zip'
shutil.unpack_archive(filepath,extract_dir='E:\\x11111',format='zip')
