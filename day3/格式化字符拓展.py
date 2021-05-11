name = 'tom'
age = 22
weight = 64.5
# 我的名字是x，今年x岁了，体重是x公斤
# 针对字符串做的拓展
# 不管x是什么类型的数据，最后在print中输出的结果都是以字符串的形式输出的
print('我的名字是%s，今年%s岁了，体重是%s公斤' % (name, age, weight))

# f'{表达式}'格式化字符串
print(f'我的名字是{name}，今年{age}岁了，体重是{weight}公斤')
print('hello\nworld')
print('\tabcd')


# print结束符号：一般来讲，print默认的结束符号是\n
# 因为每次print用完之后，都要换行之后执行下一个print
print('hello', end='\n')
print('world', end='\t')
print('hello', end='...')
print('python')
print('hello world')