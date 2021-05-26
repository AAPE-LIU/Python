# 字符串的修改
mystr = 'if you do not strong enough you will die'
# 1.replace():替换
# 字符串序列.replace(旧子串，新子串，替换次数)
# replace()把you替换成him
mystr.replace('you', 'him')
print(mystr)  # 这里并没有打印替换之后的字符串
new_str = mystr.replace('you', 'him')
print(new_str)  # 这里就会打印替换之后的字符串
# ********** 调用了replace函数后，发现原有的字符串的数据并没由做到修改
# 修改之后的数据是replace的返回值
# ---说明  字符串是不可变数据类型
# 列表和字典都是可以直接修改的数据
# 数据是否可以改变划分为两大类  可变类型  和   不可变类型
new_str2 = mystr.replace('you', 'him', 1)
print(new_str2)  # 只替换第一个you

new_str3 = mystr.replace('you', 'him', 10)  # 替换两个you
# 如果替换次数超过了子串在字符串中出现的次数就默认全部替换
print(new_str3)

# 2.split()---分割， 返回类型是列表，会丢失分隔符
# 字符串序列.split(分割字符，num)
# num表示分割字符出现的次数，即将来返回数据个数为num+1个
new_spl1 = mystr.split('n')
print(new_spl1)  # ['if you do ', 'ot stro', 'g e', 'ough you will die']
# 分割字符并不会出现在打印结果中
new_spl2 = mystr.split('n', 2)
print(new_spl2)  # ['if you do ', 'ot stro', 'g enough you will die']


# 3.join()：合并列表里面的字符串数据为一个大字符串
# 字符或子串.join(多字符组成的系列名)
mylist = ['aa', 'bb', 'cc']
# 我想输出成aa...bb...cc
new_list1 = '...'.join(mylist)
print(new_list1)

# 4.capitalize():将字符串中第一个字符变成大写，其他字母全部小写
# 5.title():将字符串每个单词首字母转换成大写
# 6.lower():将字符串中大写转小写
# 7.upper():将字符串中小写转大写
str = 'Big city Has So manY beAutiful girL'
new_str4 = str.capitalize()
print(new_str4)  # 只有第一个字母还是大写，其余全部小写

new_str5 = str.title()
print(new_str5)  # 每个单词首字母都变成了大写

new_str6 = str.lower()
print(new_str6)  # 所有字母全部变成了小写

new_str7 = str.upper()
print(new_str7)  # 所有字母全部变成了大写
