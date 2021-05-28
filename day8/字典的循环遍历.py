# 字典的循环遍历
#1. 遍历字典中的key
dict1 = {'name': 'TONY', 'age': 33, 'gender': '男'}
for key in dict1.keys():
    print(key)
print('*******')

# 2.遍历字典的value
for value in dict1.values():
    print(value)
print('*******')

# 3.遍历字典中的元素
for item in dict1.items():
    print(item)
print('*******')

# 4.遍历字典的键值对：遍历键值对并且拆包
# xx.items():返回可迭代对象，内部是元组，元组有2个数据
# 元组数据1是字典的key，元组数据2是字典的value
for key, value in dict1.items():
    print(f'{key} = {value}')
    print(key)
    print(value)