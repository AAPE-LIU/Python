'''===============================有序字典长什么样呢？================================'''
from collections import OrderedDict
dict1 = OrderedDict()
dict1['name'] = '刘小港'  # 这里dict1是一个对象，他的后面有这种赋值语法，肯定包含__setitem__方法
dict1['age'] = 24
dict1['age']  # 这里肯定有__getitem__方法
print(dict1.keys())
print(dict1.values())