'''
while 条件:
    条件成立需要执行的代码
    .......
    .......
'''
# i = 0
# while i < 5:
#     print('你是小猪猪')
#     i += 1
# 应用：计算从1-100累加和
i = 0
sum = 0
while i < 100:
    i += 1
    sum += i
print(sum)

# 应用：1-100以内的偶数做累加和
j = 0
result = 0
while j < 100:
    j += 2
    result += j
print(result)
# 方法二：取余2看是否为0，如果为0则可以加入运算
j = 0
result = 0
while j < 100:
    j += 1
    if j % 2 == 0:
        result += j
print(result)
