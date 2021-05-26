# startswith():判断字符串是否以某个字串开头
# endswith():判断字符串是否以某个子串结尾
# 1.语法： 字符串序列.startswith(子串，开始位置下标，结束位置下标)
mystr = 'Big city has so many beauty'
print(mystr.startswith('Bi'))
print(mystr.endswith('tya'))
print(mystr.endswith('ty'))
print(mystr.find(' ma'))
print(mystr.endswith('so', 0, 15))
print('-----------')

# 1.isalpha():如果一个字符串中至少有一个字符并且所有字符都是字母
#           则返回True，否则返回False
# 2.isdigit():如果字符串中只包含数字则返回True否则返回False
mystr1 = """hello"""
mystr2 = '''hello   '''
mystr3 = '''hello12345'''
print(mystr1.isalpha())
print(mystr2.isalpha())  # 空格不算是字母
print(mystr3.isalpha())
print("-----------")
mystr4 = '123456'
mystr5 = '1234mju'
print(mystr4.isdigit())
print(mystr5.isdigit())
print('------------')
# 3.isalnum():字符串中是数字或者字母或者数字字母的组合
print(mystr5.isalnum())

print('-------------')
# 4.isspace():如果字符串中全是空格，则返回True，否则返回False
mystr6 = '       a            '
mystr7 = '                    '
print(mystr6.isspace())
print(mystr7.isspace())