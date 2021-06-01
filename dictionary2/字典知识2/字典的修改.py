d2 = {'bob': 98, 'lucas': 88, 'lily': 92}
print(d2)
# d2['lili'] = d2['lily']
# print(d2)
# d2.pop('lily')
# print(d2)
# 上述步骤就做成了键值的修改
# 可以简化为1步
d2['lili'] = d2.pop('lily')
print(d2)