'''
注意：文件中的读与写分别是指，将文件从磁盘读取到内存中，将文件从内存中写入到磁盘上
'''
file_objecct = open('log.txt',mode='r',encoding='utf-8')
# 如果碰到了很大的文件，不能一下全部读入吧，不然内存就被占满了，这样很不好
# 因此我们可以一点一点的去读
for line in file_objecct:
    print(line)  # 这样打印会有回车
    line2 = line.strip()  # strip()可以去除空格也可以去除回车
    print(line2)
file_objecct.close()
file_objecct = open('log.txt',mode='w',encoding='utf-8')  # w模式会先将文件内部的东西先清空
# 然后再写
file_objecct.write('小黑\n')
file_objecct.write('打篮球')
file_objecct.close()  # 写完之后一定要记得关闭，否则，就像你写了一大堆文档但是没保存一样
