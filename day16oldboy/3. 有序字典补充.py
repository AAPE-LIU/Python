'''可以通过这种方式去创建字典[(),(),()]'''
from collections import OrderedDict
dict1 = OrderedDict([('name','刘总'),('age',22),('gender','male')])
print(dict1)
for i,j in dict1.items():
    print(i,j)