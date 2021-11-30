'''
map() :循环每个元素(第二个参数)，然后让每个元素执行函数(第一个参数)，将每个函数执行的结果
        保存到新的列表中，并返回。map中的第二个参数，必须是一个可迭代对象
        第一个参数是一个函数，函数的传入参数就是迭代第二个参数得到的每一个元素
'''

# map()
list1 = [1,2,3,45]
def func(x):
    return x + 100
result = map(func,list1)
print(result)  # 但是python3中并不会直接输出结果，只会将返回值存储到一个新的列表中，然后当你去
# 迭代这个列表的时候才会将返回值显现出来，就比如说强制转换为list类型
print(list(result))

def func1(x):
    print(x)
result = map(func1,list1)
print(result)
print(list(result))
print(list1)  # [1, 2, 3, 45] map是有返回值的并不会影响原列表
print('=================================')
# 这样看还不如用for循环来的方便，因此可以将map与lambda结合
list2 = [7,45,51,42]
result = map(lambda x : print(x),list2)
print(list(result))

'''
filter()同样第一个参数是函数，第二个参数是一个可迭代对象，如果函数返回True则将此迭代元素
放到用于接收的列表中，如果返回False就丢弃，
'''
# filter():
# 将list3中的数字筛选出来，不要字符串
list3 = [25,33,12,'kgfhj','iretu',7]
result = filter(lambda x : type(x) == int, list3)
result2 = filter(lambda x :True if type(x) == int else False,list3)
print(list(result))
print(list(result2))

'''
reduce():reduce函数第一个函数仍然是一个函数，第二个参数仍然是一个可迭代对象，只不过在执行
函数的时候，第一次会直接取两个值，然后将返回值作为第二次迭代的一个参数，再加上可迭代对象
中的一个参数，又构成了俩参数，传入函数进行运算，由于最后计算出来是一个值，因此就不需要
存入一个空数组之类的操作了，就直接打印，或者调用就可以
'''

