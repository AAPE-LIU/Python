'''
首先要明确的是，如果直接在源文件中修改，是不可以的，因为文件写好了之后是顺序存储在
内存中的，如果将源文件内容修改的话，需要修改相同的字节数，否则后面的字节移动量太大了
因此提供以下两种方式进行修改
'''
# 方式一：将文件先读入内存，在内存中进行修改，然后再重新写到磁盘上去
with open('log.txt',mode='r',encoding='utf-8') as v:
    f = v.read()
new_data = f.replace('你','二哈')
with open('log.txt',mode='w',encoding='utf-8') as v:
    v.write(new_data)

# 一些重要的问题
with open('log.txt',mode='r',encoding='utf-8') as v:
    f = v.read()
    print(type(v))  # <class '_io.TextIOWrapper'>
    print(type(f))  # <class 'str'>
    print('====================================')
    print(v)  # <_io.TextIOWrapper name='log.txt' mode='r' encoding='utf-8'>
    for i in f:  # 如果打开的文件，已经被读取了，再用for循环循环这个接收打开的文件（v）就没用了
        print(i) # 此时for循环可以循环用来接收读取过后的文件，但是是一个字符一个字符的去循环
    print('====================================')
    for i in v:  # 这里如果用来循环的话，什么都不会显示，打开的文件已经被读取到内存中去了
        print(i)
with open('log.txt', mode='r', encoding='utf-8') as v:
    print(type(v))  # <class '_io.TextIOWrapper'>
    for i in v:
        print(i)

# 方式二：现在试想这样一种情况，如果有一个很大的文件，四五十个G，你如何用第一种方法？
# 你如何将四五十个G的文本一下读入到内存中去？
'''
因此又有了第二种方法，一行一行地读，然后一行一行地将他写入到另外一个空文件中
'''
with open('log.txt',mode='r',encoding='utf-8') as v:
    with open('save.txt',mode='w',encoding='utf-8') as s:
        for line in v:
            new_data = line.replace('二哈','哈士奇憨憨')
            s.write(new_data)  # write虽说每次写文件前都会把文件内容清空
# 但是那只是打开文件的第一次写入，如果文件打开了没有关闭，写多少次，都会从上一次的结尾处开始写
with open('log.txt',mode='r',encoding='utf-8') as v,open('save.txt',mode='w',encoding='utf-8') as s:
    # python目前支持这种写法，还是很nice的
    for line in v:
        new_data = line.replace('二哈','哈士奇憨憨')
        s.write(new_data)