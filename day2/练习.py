'''
请输出所有的键和值，并且根据用户输入name/age/gender/hobby输出对应的结果
'''
info = {'name':'刘总','gender':'男','age':22,'hobby':'badminton'}
for i,j in info.items():
    print(i,j)

a = input('请输入你要查询的信息：name/age/gender/hobby:')
print(info[a])

'''
给定一个空字典，在空字典中添加数据'k1':1,'k2':2,'k3':4,'k4':8
'''
dict = {}
dict['k1'] = 1
dict['k2'] = 2
dict['k3'] = 4
dict['k4'] = 8
for i,j in dict.items():
    print(i,j)

'''
如果给你一个message = "k1|v1,k2|v2,k3|123"
想把它生成为一个字典，该怎么做？
'''
message = "k1|v1,k2|v2,k3|123"
dict = {}
for i in message.split(','):
    # print(i)
    j,k = i.split('|')
    dict[j] = k
for i,j in dict.items():
    print(i,j)