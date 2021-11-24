list = ['alex','wuqian','rita','barry','beijing']
list.append('seven')
print(list)
list.insert(1,'Tony')
print(list)
list.insert(2,'Kelly')
print(list)
list[3] = '太白'
print(list)
list2 = [1,"a",3,4,'heart']
for i in list2:
    list.append(i)
print(list)
list.append(list2)
print(list)  # 从这里可以看出，append是以元素为单位添加，将整个序列作为一个元素添加进去
list.remove('rita')
print(list)

# 如果要将一个字符串或者列表这种序列中的单个元素添加进另一个列表中，并且不允许循环实现
# 用一行代码，该怎么做？？
str = 'lksahdfiahs'
list.extend(str)  # extend的功能其实是，将序列中的每一个元素遍历，然后添加进新的序列中去
print(list)
'''
del和pop的区别
'''
print('================================')
returnNum = list.pop(3)
print(list)
print(returnNum)
del list[3]
print(list)

'''
实现字符串"小黑半夜三点在玩愤怒的小鸡"的倒序
'''
str = "小黑半夜三点在玩愤怒的小鸡"
value = str[::-1]
print(value)

str1 = "小黑半夜三点在玩愤怒的小鸡"
value1 = ''
str1_length = len(str1)
while str1_length > 0:
    value1 += str1[str1_length-1]
    str1_length -= 1
print(value1)

str2 = "小黑半夜三点在玩愤怒的小鸡"
value2 = ''
length = len(str2)
for i in str2 :
    value2 += str2[length-1]
    length -= 1
print(value2)

str3 = "小黑半夜三点在玩愤怒的小鸡"
value3 = ''
for i in range(len(str3),0,-1):
    value3 += str3[i-1]
print(value3)

'''
打印0-100之间的偶数
'''
for i in range(0,101,2):
    print(i,end=' ')
print()
for i in range(100,-1,-2):
    print(i,end=' ')
print()

'''
输入数字，输出对应的输入-1下标的商品
'''
goods = ['飞机','大炮','火箭']
# while True:
#     nob = input('请输入编号：')
#     if nob.isdigit() & int(nob)<4 & int(nob)>0:
#         nob1 = int(nob)
#         print(goods[nob1-1])
#     else:
#         print('输入有误')

'''
1
(1)
(1,)
上面三个分别是什么类型？
int, int, tuple
'''
a = [(1),(2),(3)]
# 等价于
a = [1,2,3]
