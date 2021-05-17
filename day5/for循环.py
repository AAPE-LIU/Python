# for循环格式：
# for 临时变量 in 序列:
#   重复执行的代码1
#   重复执行的代码2
#   ......
str1 = 'liuxiuda'
for i in str1:
    if i == 'x':
        print('遇到了x不打印')
        continue
    print(i)
else:
    print('正常结束')

# while....else的用法
# 只有当while正常执行结束之后才能执行else中的语句
i = 0
while i < 6:
    if i == 5:
        i += 1
        continue
    print('你是猪')
    i += 1
else:
    print('我原谅你了')