'''
编译器：将所有代码进行整体编译，然后整体放到计算机中去运行，有一行代码出错，整体都不会运行
解释器：解释器是一行一行代码进行编译然后放到计算机中去运行，
        即使下面有代码出错了，上面没出错的也会运行
'''

'''
unicode
utf-8
'''
name = '李杰'  # 解释器读取到内存后，按照unicode编码存储：8个字节，每个字符4字节
v1 = name.encode('utf-8')  # 每个字符，utf-8占三个字节
print(v1)  # b'\xe6\x9d\x8e\xe6\x9d\xb0'
v2 = name.encode('gbk') # 每个字符，gbk编码占用2个字节
print(v2)  # b'\xc0\xee\xbd\xdc'