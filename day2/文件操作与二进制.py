# 方式一：一般适用于文本写入
f = open('log.txt',mode='w',encoding='utf-8')
'''
f.write写入文件的步骤：
a：将要写入的内容按照指定的编码格式进行二进制的转换，然后将二进制写入到文件当中
'''
f.write('你好啊')
f.close()

# 方式2：一般适用于图片，音频，视频，未知编码
f2 = open('log.txt',mode='wb')  # wb是指以二进制的方式进行写入文件
# f2.write('我饿了')  # TypeError: a bytes-like object is required, not 'str'
# 计算机又不知道你是以什么编码格式进行二进制的编写，而且给的是str类型
data = '我饿了'
content = data.encode('utf-8')
f2.write(content)
f2.close()
f2 = open('log.txt',mode='r',encoding='utf-8')

print(f2.read())
print(f2.tell())  # 获取当前光标所在的字节位置