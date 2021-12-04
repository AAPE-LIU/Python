'''
适用于数据量特别大的情况下，比如将100亿条 数据取出来，显示在我的电脑上
就要一点一点地去取，这就用到了生成器
'''
'''
函数中如果存在yield，那么该函数就是一个生成器函数，调用生成器函数会返回一个生成器
生成器只有被for循环的时候，生成器内部的代码才会执行，每次循环都会获取yield返回的值
'''
# 没有yield，因此这只是一个普通的函数，执行函数，函数内部的代码就会被执行
def func1():
    print(123)
func1()

# 包含yield 因此是一个生成器，生成器中，每次循环只会取一个yield，下次循环的时候从上次结束的位置继续
def func2():
    print('F1')
    yield 1

    print('F2')
    yield 2

    print('F3')
    yield 3

    print('F4')
    yield 4
gene = func2()
for item in gene:
    print(item)

print('===========================================')
def func3():
    count = 0
    while count <= 100000:
        yield count
        count += 1
gene2 = func3()
for item in gene2:
    print(item)
'''==============================================='''
def func4():
    return 1111
    yield 3
    yield 4
    yield 5
v = func4()
for item in v:
    print(item)  # 什么都不打印，为什么呢？因为item只拿yield中的值，但是执行到return就结束了，所以什么都不打印
