'''
list1 = [12,24,32,15]
迭代器：帮助你对某种对象（str/list/tuple/dict/set）[也称为序列]中的元素进行逐一获取。
迭代器：对对象进行迭代，器，只是一种工具
列表转换成迭代器：v1 = iter(list1)或者v1 = list1.__iter__()
取下一个元素：v1.__next__()
'''
list1 = [12,24,32,15]
ite1 = iter(list1)
# v1 = ite1.__next__()
# print(v1)
# v1 = ite1.__next__()
# print(v1)
# v1 = ite1.__next__()
# print(v1)
# v1 = ite1.__next__()
# print(v1)
# v1 = ite1.__next__()
# print(v1)  # 取完了再取就会报错，如果想不让他报错，就可以用异常处理

while True:
    try:
        v = ite1.__next__()
        print(v)
    except Exception as e:
        break  # 这里写break也可以
'''
如何判断一个对象是否是迭代器：内部是否有__next__()方法，如果有，就是迭代器
'''
'''
如何判断可迭代对象：
内部是否具有__iter__()方法，具有这个方法的才是可迭代对象
'''
'''for循环的内部就是使用的迭代器'''