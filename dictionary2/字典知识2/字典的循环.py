d1 = {'name': '刘小总', 'age': 22, 'salary': 30000}
for x in d1.keys():
    print(x)
for x in d1.values():
    print(x)
for x in d1.items():
    print(x)
for x, y in d1.items():
    print(x,y)

# 但是有时候不想循环，就想把他们都显示在一起
# 字典在列表中的推导
l1 = [x for x in d1];print(l1)
l2 = [x for x in d1.values()];print(l2)
l3 = [x for x in d1.items()];print(l3)

# 对字典的重新推导
d2 = {y:x for x, y in d1.items()}  # 把冒号前面的作为键名
d3 = {y:2 for y in d1.items()}
d4 = {y[0]:2 for y in d1.items()}
print(d2)
print(d3)
print(d4)
# 其他结构的推导为字典
p1 = ['张三', 'lisi', 'wangwu']
p2 = [198, 199, 200]
d5 = {x:y+10 for x,y in zip(p1,p2)}
print(d5)