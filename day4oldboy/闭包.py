'''
函数作为返回值
闭包：为函数创建一块区域（内部变量供自己使用），为他以后执行数据
episode 125
函数是由谁创建的，以后的作用域的上一级就要从谁开始找
'''
name = 'alex'
def base():
    print(name)
def bar():
    name = 'eric'
    base()
bar()
# 问打印的是什么？
name2 = 'alex'
def base2():
    name2 = 'eric'
    def bar2():
        print(name2)
    return bar2
v = base2()
v()

name3 = 'alex'
def fun3():
    name3 = 'eric'
    def base3():
        print(name3)
    return base3
base3 = fun3()
base3()

info = []
def func(i):
    def inner():
        print(i)
    return inner
for item in range(10):
    info.append(func(item))
info[0]()
info[2]()
info[4]()
# ########################################
'''
函数不被调用，内部代码永远不被执行
'''
func_list = []
for i in range(10):
    func_list.append(lambda : i)
print(func_list[0]())

'''
执行函数是，会信创建一块内存保存自己函数执行的信息 => 闭包
'''
print('==================================')
def base():
    return i

def func8(args):
    def innner():
        return args
    return innner

list_1 = []
list_2 = []
for i in range(10):
    list_1.append(base)  # 这个列表里面存储的是base的地址，他是在全局创建的
    list_2.append(func8(i))  # 这个列表里面存储的是inner的地址，他是由func()执行时创建的

for item in list_1:
    print(item(),end=' ')
print()
for item in list_2:
    print(item(),end=' ')
print('=============================')


# 看代码分析结果
func_list1 = []

for i in range(10):
    func_list1.append(lambda x:x + i)

print(func_list1[2](1))  # 要我写的话，我写10
print(func_list1[4](9))  # 要我写话我写18

'''
如果还不懂就去看episode141的习题讲解
'''