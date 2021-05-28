dict1 = {'name': 'TONY', 'age': 33, 'gender': '男'}
# 1.序列名[key]
print(dict1['name'])  # 返回对应的值(key存在)
# print(dict1['names'])  # 报错，对应的key不存在

# 2.函数
# 1.get():
# 语法：字典序列.get(key, 默认值)
# 如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回NONE
print(dict1.get('name'))  # 返回Tony，找到了key
print(dict1.get('names', 'bb'))  # 返回bb，没有找到key
print(dict1.get('names'))  # 没有写参数返回None
# 2.keys()--查找字典中所有的key，返回可迭代对象
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])
# 上述显示方式，是一个可迭代的对象，可以用for控制，遍历的一个对象


# 3.values()--查找字典中所有的value，并且返回一个可迭代的对象
print(dict1.values())  # dict_values(['TONY', 33, '男'])

# 4.items()--查找字典中所有的键值对，返回可迭代对象，里面的数据是元组
# 元组数据1是字典中的key，元组数据2是字典中的value
print(dict1.items())