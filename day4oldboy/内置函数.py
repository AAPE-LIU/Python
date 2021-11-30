'''
已经学过的内置函数：
len()
open()
range()
id()
type()
输入输出：
    print()
    input()
强制转换：
    dict()
    list()
    tuple()
    str()
    int()
    set()
    bool()
    float()
数学相关：
    abs() ,绝对值
    max() ,求最大值
    min() ,找最小值
    sum() ,求和
    divmod() ,两数相除的商和余数
    round() ,指定保留几位小数
进制转换相关：
    bin() ,将其他数据类型转换为二进制
    oct() ,将其他进制转换成八进制
    int() ,将其他进制转换为十进制
    hex() ，将其他进制转换为十六进制
转换成二进制，八进制，十六进制，传入的参数只能是int型的，所以如果二，八，十六之间
想互相转换，只能先转换为十进制，然后由十进制再转换为其他类型的
'''
a,b = divmod(5,3)
print(a,b)

list1 = [12,45,3,84,1,24,51,75,312,2,4]
x = max(list1)
print(x)
y = min(list1)
print(y)
'''
分页展示案例episode117
'''

num = 15
x1 = bin(num)
print(x1)
x2 = oct(15)
print(x2)

# 十六进制转十进制,表示非十进制一般用字符串表示，然后再转换成int，可以设置base，即是什么进制
# 其实，也可以直接写
num2 = '0xf'
x3 = int(num2,base=16)
print(x3)
num3 = 0xf
x3 = int(num3)
print(x3)

a = round(1,234)  # 默认不保留小数
print(a)
a = round(1.38476958, ndigits=4)
print(a)