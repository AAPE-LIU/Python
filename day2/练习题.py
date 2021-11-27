'''
请将user = ['alex','eric']用下划线连接起来，并写入文件
'''
user = ['alex','eric']
str1 = '_'.join(user) + '\n'
file = open('log.txt',mode='w',encoding='utf-8')
file.write(str1)
file.close()

'''
user = [
{'user':'alex','pwd':'123'},
{'user':'eric','pwd':'oldboy'}
]
将这里面的数据格式转换成alex|123这种类型的，并写入到文件中去
'''
f = open('log.txt',mode='a+',encoding='utf-8')  # a+类型，是追加，可读可写，但是每次执行
# 写操作的时候，光标总会移动到最后一个字符的位置，读取文本的时候，还要用seek将光标
# 给移动到指定位置开始读
user = [
{'user':'alex','pwd':'123'},
{'user':'eric','pwd':'oldboy'}
]
for i in user:
    list = []
    for val in i.values():
        list.append(val)
    str = '|'.join(list) + '\n'
    f.write(str)
f.seek(0)
for i in f:
    print(i,end='')
f.close()