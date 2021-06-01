d1 = dict(a=1,b=2,c=3)
print(d1)
d2 = dict((('a', 1),('b', 2)))
print(d2)
# 其实内部可以元组和列表随意组合
# ( [], [] )或者（ （），（））或者[ (), () ]或者[ [], [] ]
# 还可以像下述这种方法一次性转换
d3 = dict(zip(['h', 'j', 'k'], [1, 2, 3]))
print(d3)

k = ['v', 'b', 'd']
n = [1, 2, 3,]
print(dict(zip(k,n)))  # 这种是可以打印的

# 但是如果k,n已经组合起来了呢
l = [['v', 'b', 'd'], [1, 2, 3,]]
print(dict(zip(*l)))  # 针对这种情况只需要用一次*反解即可


# dict.fromkeys方法--包含两部分数据，第一部分是key，第二部分是value
d5 = dict.fromkeys(['a', 'b', 'c', 'e'], 1)
print(d5)