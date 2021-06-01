d = {'name': '曾小贤', 'age': 22, 'salary': 110000}
# d.clear()
# print(d)


# pop方法删除指定的某一对，只需要指定键名就可以
# d.pop('name')

# popitem方法删除时，不需要指定键名，随即删，不过一般就删除最后一个
# d.popitem()
# print(d)

# del删除方法
del d['age']
print(d)