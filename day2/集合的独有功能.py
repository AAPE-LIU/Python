set1 = {1,2,3,4}
# add
set1.add('刘总')
print(set1)

# discard
set1.discard(1)
print(set1)

# update
set1.update({4,3,5,'liuxiaogang'})
print(set1)
'''
下面所有的操作，括号内部的对象，不一定非得是集合，列表，元组都可以
'''
# intersection()  求两者之间的交集
set2 = {2, 3, 4, '刘总', 5, 'liuxiaogang'}
set3 = { 3, 4, '刘总', 'liuxiaogang','liuxiaozong',67}
result = set2.intersection(set3)
print(result)

# differencce()  求差集
result = set2.difference(set3)
print(result)

# 求交叉差集
result = set2.symmetric_difference(set3)
print(result)

# 那么求并集也就好求了，求出来交叉差集之后，再加上交集就是并集了

set4 = {1,2,3,4,5,6,True,False,0}
print(set4)  # {False, 1, 2, 3, 4, 5, 6}
# 这里True和1，False和0 都只能随机留下一个，因为True会被解析为1，Fasle被解析成0
