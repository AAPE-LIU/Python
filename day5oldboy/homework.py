'''
如果让你交换a，b的值该怎么做？
'''
a = 2
b = 1

temp = a
a = b
b = temp
print(a,b)
# 还有一种方法
a = 2
b = 1
a,b = b,a  # 这个式子和上面的函数内部实现完全一样
print(a,b)

'''
编程实现400万以内最大的斐波那契数
'''
a = 1
b = 1
while a < 4000000:
    a,b = a+b,a
print(b) 