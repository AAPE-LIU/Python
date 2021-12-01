'''
这种题目有陷阱
'''

# 不推荐==============================
def func(data,value = []):
    value.append(data)
    return value

value1 = func(1)
print(value1)  # [1]

'''
这里为什么会是[1,2]呢？
原理见QQ截图
'''
value1 = func(2)
print(value1)  # [1, 2]

value = func(3,[12,3,5,6])
print(value)  # [12, 3, 5, 6, 3]

print(value1)  # [1, 2]

print('========================================')
def func1(a,b = []):
    b.append(a)
    return b

l1 = func1(1)
l2 = func1(3,[12,3,45,5])
l3 = func1(9)

print(l1,l2,l3)  # 要搞清楚，打印是最后一步，前面已经把列表创建好了


# 推荐===================================
def func1(a,b = None):
    if not b:
        b = []
