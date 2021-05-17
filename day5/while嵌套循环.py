# j = 0
# while j < 3:
#     i = 0
#     while i < 3:
#         print('老子天下第一')
#         i += 1
#     print('好好学习，天天向上')
#     print(f'第{j+1}套连招结束！')
#     j += 1
#
# # 打印三角形排列的*
# i = 0
# while i < 5:
#     i += 1
#     j = 0
#     while j < i:
#         print('*', end='')
#         j += 1
#     print('\n')

# 打印9*9乘法表
i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        # 也可以这样写
        print(f'{j} * {i} = {j*i}', end='\t')
        # print('%d * %d = %-2d' % (j, i, i*j), end='   ')
    print('\n')