'''
对于列表以及元组，或者字典来说，当取值的时候，下标或者键不存在就会报错
因此在公司中对字典取值有另外的一种方法，get方法，这种方法并不会报错，如果取到了
所给的关键字对应的值的信息，那么就会得到对应的值，否则就会返回你所指定的返回值
'''
dict1 = {'k1':1,'k2':2}
# print(dict1['lkshdfk'])  # KeyError: 'lkshdfk'
print(dict1.get('kdfasd','没有这个键'))  # 没有这个键

# pop  del
result = dict1.pop('k1')
print(dict1)
print(result)

# updata
dict1.update({'k2':4,'k3':6,'k4':7})
print(dict1)
