# 输出hello world  快捷键ctrl + /
print("hello world")
print("jello python")  # 一般如果在代码后面注释的话，需要
# 先输入两个空格之后才能输入#加空格进行注释，一般用于精简情况
# hello world
"""
第一行注释
第二行注释
第三行注释
"""

'''
第一行注释
第二行注释
第三行注释
'''
my_name = 'liuzong'
print(my_name)
herName = '我是程序员'
print(herName)
num1 = 1
num2 = 1.1
print(type(num1))
print(type(num2))
a = 'hello world'
print(type(a))
b = True
print(type(b))

c = [10, 20, 30, 50]  # 列表类型
print(type(c))
d = (10, 20, 30)  # 元组类型
print(type(d))

e = {10, 20, 30}  # 集合类型
print(type(e))

f = {'name': 'tom', 'age': 23}
print(type(f))

'''
格式化输出
'''
# 格式化符号 %s %d %f
# 今年我的年龄是x岁
# 我的名字是x
# 我的体重是x公斤
# 我的学号是x
# 我的名字是x。今年x岁了
age = 18
name = 'tom'
weight = 64.5
schoolNum = 2016214445
schoolNum2 = 1
# print('今年我的年龄是%d岁')这样是肯定输出不了的，因为没有和变量连接起来
print('今年我的年龄是%d岁' % age)
print('我的名字是%s' % name)
print("我的体重是%.2f公斤" % weight)  #这样写是让小数点后保留两位小数
print('我的学号是%d' % schoolNum)

# 输出我的学号是001
print('我的学号是%03d' % schoolNum2)
print('我的学号是%03d' % schoolNum)
# %03d表示输出的整数显示位数，不足以0补全，超出则原样输出
print('我的学号是%3d' % schoolNum2)
print('我的学号是%3d' % schoolNum)
print('我的学号是%-3d' % schoolNum2)
# 而%3d表示占用至少三个位置，不足就以空格填充在前
# 超出就原样输出
# %-3d表示填充在后

print('我的名字是%s。今年%d岁了' % (name, age))

print('我的名字是%s。明年%d岁了' % (name, age+1))
# 我的名字是x，今年x岁了，体重是x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重是%.2f公斤，学号是%03d' % (name, age, weight, schoolNum))
