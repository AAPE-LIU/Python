import re

# regex ,正则的英文

result = re.findall('\d','932849872398jhsdfu8298')
print(result)
# findall会匹配字符串中所有符合规则的项
# 并且会返回一个列表
# 如果未匹配到则返回一个空列表
result1 = re.search('\d','932849872398jhsdfu8298')
print(result1)  # <re.Match object; span=(0, 1), match='9'>
print(result1.group())  # 9
# 为什么只匹配到一个9呢？
# re.search只会从头到尾从待匹配的匹配字符串中取出第一个符合条件的项
# 如果匹配不上就会报错

# 如果不想让他报错的话，就可以这样
result1 = re.search('\d','932849872398jhsdfu8298')
print(result1)  # <re.Match object; span=(0, 1), match='9'>
if result1:  # 如果返回的结果是None的话就不会进入调用group这个环节
    print(result1.group())  # 9
# 会从头到尾从待匹配匹配字符串中取出  第一个  符合条件的项
# 如果匹配到了返回一个对象，用group取值
# 如果没匹配到返回一个None

ret = re.match('\d','932849872398jhsdfu8298')  # None
print(ret)  # <re.Match object; span=(0, 1), match='9'>

# match这个方法你知道就可以，完全可以理解为  search + ^ 正则表达式
ret = re.match('\d','ab932849872398jhsdfu8298')
print(ret)  # None
# match相当于自动给search中的正则表达式加上了一个 ^
# 他总是从头开始匹配 符合匹配条件的字符串，如果开头不符合，那么就不再继续匹配
# 如果符合就返回对象，用group取值
# 如果不符合就返回None
