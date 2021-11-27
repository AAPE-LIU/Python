'''
info.keys()  暂且认为他返回的是一个列表，其实并不是列表
info.values()
info.items()
'''
info = {'name':'刘总','gender':'男','age':22}
for i in info.keys():
    print(i)
print('================================')
for i in info.values():
    print(i)
print('================================')
for i,j in info.items():
    print(i,j)

'''
修改字典
'''
# 改值
info['age'] = 18
print(info['age'])
# 改键
# 键一般是不修改的，如果实在想修改，就把原来的键值对删除，然后再新添加一个，反正也是无序的
del info['age']
info['myage'] = 19  # 如果字典中不存在关键字，那么就会直接添加进字典
for i,j in info.items():
    print(i,j)