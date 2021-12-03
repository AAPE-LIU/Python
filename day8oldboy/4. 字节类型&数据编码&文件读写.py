'''
比如有个字符串 v1='张三' ，在内存的内部存储的时候其实是用Unicode编码存储的的二进制，每个字符占4个字节
这种字符串可以通过encode进行编码的，以jbk或者utf-8的形式进行编码，v2 = v1.encode('utf-8')
这种经过编码得到的东西，一般我们称之为字节，字节类型，一般以b开头
我们写文件的时候，进行网络传输的时候，本质上写的传的就是这种经过编码之后的东西
'''
f = open('log3.txt',mode='wb')  # 表明以二进制写入
data = 'asjkdhgkj'.encode('utf-8')  # 表明编码为utf-8类型，是二进制文件
f.write(data)  # 写入
f.close()
'''=========================================='''
f = open('log4.txt',mode='w',encoding='gbk')  # 内部进行的是转成字节再进行存储
f.write('lksdhfgiushdf;kighspdof你好啊')
f.close()
'''=============================================='''
f = open('log4.txt',mode='r',encoding='gbk')  # 读取的时候不管是写gbk还是utf-8都可以正确读取出来,
data = f.read()
print(data)
f.close()