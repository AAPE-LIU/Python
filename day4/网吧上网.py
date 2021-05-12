# # 易错点！注意！
age = int(input('请输入年龄：'))
# if age >= 18:
#     print('已经成年可以上网', end='···')
# else:
#     print(f'您输入的年龄是{age}，小朋友，回家写作业去')
# print('系统关闭')

if age < 18:
    print(f'您的年龄是{age}，小屁孩一个，滚回去读书')
# elif (age >= 18) and (age <= 60):
# python中还可以这样书写？！
elif 18 <= age <= 60:
    print(f'您的年龄是{age}，符合工作需求，欢迎来上班')
else:
    print(f'您都老掉牙了，快回家养老去吧')