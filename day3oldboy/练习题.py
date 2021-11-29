# def sum_dig(list1):
#     count = 0
#     for i in list1:
#         if type(i) == int:
#             count += 1
#     return count
# list = ['sdf','vf',12,34,65,'kdjh',True,False]
# num = sum_dig(list)
# print('列表中有%d个数字'%(num,))

'''
读取文件，将文件的内容构造成指定格式的数据并返回
a.log文件
    alex|123|18
    eric|uiuf|19
目标结构：
a.['alex|123|18',eric|uiuf|19]
b.[['alex','123','18'],['eric','uiuf','19']]
c.[
{'name':'alex','age','18','pwd':'123'}
]
'''
# def change_Mode(text):
#     list1 = []
#     for i in text:
#         list1.append(i.strip())
#     return list1
# with open('log.txt',mode='r',encoding='utf-8') as f:
#     list2 = change_Mode(f)
# print(list2)

# def change_Mode2(text):
#     list1 = []
#     for i in text:
#         i = i.strip()
#         list2 = i.split('|')
#         list1.append(list2)
#     return list1
# with open('log.txt',mode='r',encoding='utf-8') as f:
#     list2 = change_Mode2(f)
# print(list2)

def change_Mode2(text):
    list1 = []
    for i in text:
        dict1 = {}
        i = i.strip()
        list2 = i.split('|')
        dict1['name'] = list2[0]
        dict1['pwd'] = list2[1]
        dict1['age'] = list2[2]
        list1.append(dict1)
    return list1
with open('log.txt',mode='r',encoding='utf-8') as f:
    list2 = change_Mode2(f)
print(list2)