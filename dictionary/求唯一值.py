l = ['张三', '李四', '张三', '王五', '张三', '李四']
d = {}
for x in l:
    d[x] = ''
    print(d)
    print(list(d)) # 如果只想要键名，可以用list，list默认可以取到键名
    