import re

'''这种方法会很卡，占用内存很大'''
# ret = re.findall('\d','jkdhf8934798'*20000000)
# print(ret)

# 如果你匹配到的数据非常多，结果非常多的时候，为了防止内存爆了，占用过多，可以使用以下方法
ret = re.finditer('\d','jkdhf8934798'*20000000)
print(ret)  # <callable_iterator object at 0x000001FA52B52BE0>
for i in ret:
    print(i.group())  # 同样也是用  group  取值


'''=========================================re.compile()===================================='''
# 为了提高效率而设计出来的
# 如果有一个很长的正则表达式，而且有很多字符串需要匹配，你每进行匹配一次都需要将正则式编译一次，很浪费时间
ret = re.compile('\d+')
result1 = ret.findall('jkdhf8934798')
print(result1)
result2 = ret.search('jkdhf8934798')
print(result2)

'''
findall ：用来找所有      search ： 用来找第一个符合的
finditer ： 节省空间      compile ： 用来节省时间
'''


