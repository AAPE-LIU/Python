def func():
    cursor = 0
    while True:
        f = open('redis.txt',mode='r',encoding='utf-8')  # 为什么不能把这一句放到循环外面，一直取值呢？
        # 因为redis对于访问数量是有限制的，我访问的时候别人不能访问，为了防止一直占用资源不释放，就让文件一块一块的去读取
        # 在这里是10行10行地读取，这里用循环代替，redis中是有索引的，正常用切片[0:10]表示十行数据
        f.seek(cursor)  # 取到cursor的值，也就是光标目前的位置
        for i in range(10):
            content = f.readline()
            if not content:
                return
            yield content
        cursor = f.tell()  # 告诉cursor目前的光标在什么位置，将cursor置为那个值
        f.close()

for item in func():
    print(item)