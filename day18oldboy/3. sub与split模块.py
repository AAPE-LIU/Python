'''
sub :
split : re.split('\d','kljsdk45bnjdf23jsjfn9nnjk99')
'''
import re
ret = re.split('\d+','kljsdk45bnjdf23jsjfn9nnjk99')  # 默认自动保留分组中的内容
print(ret)  # ['kljsdk', 'bnjdf', 'jsjfn', 'nnjk', '']
# 上面的例子没有分组，因此不会保留切分出去的东西

ret = re.split('(\d+)','kljsdk45bnjdf23jsjfn9nnjk99')  # 默认自动保留分组中的内容
print(ret)  # ['kljsdk', '45', 'bnjdf', '23', 'jsjfn', '9', 'nnjk', '99', '']
# 上面将所有的数字都保存了下来

ret = re.split('\d(\d)','kljsdk45bnjdf23jsjfn9nnjk99')  # 默认自动保留分组中的内容
print(ret)  # ['kljsdk', '5', 'bnjdf', '3', 'jsjfn9nnjk', '9', '']
# 将所有的连续两个数字的第二个数字保留了下来

'''====================re.sub():用于将符合正则式的字符串全部替换为指定内容,也可以指定替换几处==================='''
ret = re.sub('\d(\d)','你是什么鬼','kljsdk45bnjdf23jsjfn9nnjk99',2)
print(ret)

'''====================re.subn()：返回一个元组元组内容是替换之后的字符串，替换的次数========================='''
ret = re.subn('\d(\d)','你是什么鬼','kljsdk45bnjdf23jsjfn9nnjk99',2)
print(ret)