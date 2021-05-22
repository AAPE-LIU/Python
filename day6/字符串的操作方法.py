# 字符串的常用操作方法
'''
find()：检测某个字串是否包含在这个字符串中，如果在返回这个字串开始位置的下标
        否则返回-1
        字符串序列.find(子串，开始位置下标，结束位置下标)
index():检测某个字串是否包含在这个字符串中，如果在返回这个字串开始位置的下标
        否则则报异常
        字符串序列.index(子串，开始位置下标，结束位置下标)
count():统计子串在字符串中出现的次数
        字符串序列.count(子串，开始位置下标，结束位置下标)
'''
# 1.find()
mystr = 'hello world I am learning python love learn very love'
print(mystr.find('wor'))  # 6
print(mystr.find('wor', 5, 20))  # 6
print(mystr.find('leram'))  # -1  learm子串不存在

# 2.index()
print(mystr.index('wor'))  # 6
print(mystr.index('learn'))  # 17
# print(mystr.index('learm'))  # 报错了

# 3.count()
print(mystr.count('learn'))  # 2
print(mystr.count('learn', 8, 20))  #

# rfind():和find()功能相同，但查找方向为右侧开始。
# rindex():和index()功能相同，但查找方向为右侧开始。
# count():返回某个字串在字符串中出现的次数

# 4.rfind()
print(mystr.rfind('python'))  # 26  下标依然以最左为0

# 5.rindex()
print(mystr.rindex('love'))  # 49

