f = open('log.txt',mode='a',encoding='utf-8')
while True:
    content = input('请输入：')
    f.write(content)  # 这样写虽然是个死循环，让你一直输入，但是并没有把输入的东西
# 写入到txt文件中去，现在还在内存中，而flush就是将内存中的东西强制写到文件中去
    f.flush()
f.close()