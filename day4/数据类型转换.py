# 转换数据类型的函数：
'''
num = input('请输入数字：')
print(num)
print(type(num))  # str类型
print(type(int(num)))  #int类型
print(type(float(num)))
print(type(str(num)))
'''
# 1.float()--将数据转换成浮点型
num1 = 1
str1 = '123'
str2 = 'lkj'
print(type(float(num1)))
print(float(num1))
print(num1)

print(type(float(str1)))
print(float(str1))

# print(type(float(str2)))
# print(float(str2))

# 2.str()--将数据转化成字符串类型
num2 = 1234
print(type(str(num2)))
print(str(num2))

# 3.tuple()--将一个序列转换为元组
list1 = {10, 20, 30}
print(type(tuple(list1)))
print(type(list1))
print(tuple(list1))

# 4.将一个序列转化为列表
t1 = (10, 11, 12)
print(type(list(t1)))
print(type(t1))
print(list(t1))

# 5.eval()--将字符串中的数据转化为她原本的类型
str2 = '1'
str3 = '1.1'
str4 = '(100, 200, 300)'
str5 = '[102, 202, 303]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))