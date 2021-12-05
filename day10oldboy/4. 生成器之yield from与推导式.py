'''
yield from 就是从这个生成器函数跳到别的生成器函数中去执行
'''
def func():
    yield 1
    yield 2
    yield 3

def func2():
    yield 7
    yield 8
    yield 9
    yield from func()
    yield 10
    yield 18

for item in func2():
    print(item)

'''===========================生成器推导式============================='''
# 列表推导式
def func():
    list1 = []
    for i in range(10):
        list1.append(i)
    return list1
# 相当于下面这一行列表生成式，这个函数只要一执行就会生成一个列表
v = [i for i in range(10)]
print(v)

# 生成器推导式
def func2():
    for i in range(10):
        yield i

v2 = (i for i in range(10))
print(v2)  # <generator object <genexpr> at 0x000001F017F08890>

for item in v2:
    print(item)

'''=========================列表推导式=========================='''
v3 = [lambda:x for x in range(10)]
for x1 in v3:
    print(x1())

print('================================================')
# 等价于如下函数
def func3():
    result = []
    for i in range(10):
        def func4():
            return i
        result.append(func4)
    return result
for item in func3():
    print(item())  # 9,9,9,9,9,9,9,9,9,9

print('===============================================')
'''==================================生成器推导式================================'''
'''生成器是循环的时候一个一个地去执行，而列表是一次性全部读入'''
v2 = (lambda: i for i in range(10))
for i in v2:
    print(i())  # 0,1,2,3,4,5,6,7,8,9

# 相当于如下函数
def func5():
    for i in range(10):
        def func6():
            return i
        yield func6

for i in func5():
    print(i())
