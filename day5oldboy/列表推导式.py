# 变量 = [for循环的变量 for循环一个可迭代对象]
list1 = [i for i in range(10)]
print(list1)

list2 = [i+100 for i in range(10)]
print(list2)

list3 = [99 if i > 5 else 55 for i in range(10)]
print(list3)

v1 = [lambda : 100 for i in range(10)]
print(v1)  # [<function <listcomp>.<lambda> at 0x000002779131A1F0>, <function <listcomp>.<lambda> at 0x000002779131A280>
print(v1[3]())  # 100

# def func():
#     return i
# list4 = [func for i in range(10)]
# print(list4[2]())

v2 = [lambda : i for i in range(10)]
print(v2[0]())

v3 = [lambda x : x*i for i in range(10)]
print(v3[0](5))
print(v3)

def num():
    return [lambda x : i*x for i in range(10)]
print([m(2) for m in num()])

'''#########################################'''
v4 = [i for i in range(10) if i > 5]
print(v4)
