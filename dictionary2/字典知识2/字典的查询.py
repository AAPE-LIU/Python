# 单值提取
d1 = {'name': '刘小总', 'age': 22, 'salary': 30000}
print(d1['name'])
print(d1.get('name'))
print(d1.get('name1','你谁啊你'))  # 如果没有查找到则返回后面设置的默认值

# 提取键名
print(d1.keys())
print(list(d1.keys()))

# 判断键名是否存在
print('name' in d1.keys())

# 取所有的值名
print(list(d1.values()))

# 如果想全部提取的话
print(list(d1.items()))

