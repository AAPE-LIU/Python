# 1.字典的增加操作
# 写法：字典序列[key] = 值
# ***如果key存在则修改这个key对应的值；如果key不存在则新增此键值对
# ***字典为可变类型
dict1 = {'name': 'TONY', 'age': 33, 'gender': '男'}
dict1['name'] = 'BANG'
print(dict1)
dict1['race'] = 'dg'
print(dict1)

# 2.字典的删除操作
# 删除字典有两种写法 1.del(要删除的字典或者关键字)
#                    2.del 字典或者字典中的关键字
# 1.
# del(dict1['name'])
# print(dict1)
# 2.
# del dict1['name']
# print(dict1)

# del(dict1)   # 这种写法是删除整个字典
# print(dict1)

# del dict1   # 这种写法是删除整个字典
# print(dict1)


# 3.clear():清空字典,这和删除字典还不一样，删除字典是直接将字典删除
# 而清空字典是将字典内的数据清空
dict1.clear()
print(dict1)

# 4.修改字典数据
# 和新增字典数据一样，只要key值是已经存在的就可以修改字典数据
