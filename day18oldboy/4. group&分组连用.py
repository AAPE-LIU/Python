import re

s1 = '<h1>wahahwahaha</h1>'
ret = re.search('<(\w+)>(.*?)</\w+>',s1)
print(ret)
print(ret.group())  # group参数默认为0 表示取整个正则匹配的结果
print(ret.group(0))  # <h1>wahahwahaha</h1>
print(ret.group(1))  # h1
print(ret.group(2))  # wahahwahaha


# 但是这样的话，如果有很多分组，那么你就可能会混乱，因此我们可以给分组取一个名字
'''=================标签格式  (?P<>)  这个就代表标签的格式，想起什么名字在尖括号里面直接写名字================'''
s1 = '<h1>wahahwahaha</h1>'
ret = re.search('<(?P<tag>\w+)>(?P<content>.*?)</\w+>',s1)
print(ret)
print(ret.group())  # group参数默认为0 表示取整个正则匹配的结果
print(ret.group(0))  # <h1>wahahwahaha</h1>
print(ret.group('tag'))  # h1
print(ret.group('content'))  # wahahwahaha

'''================================分组的引用============================='''
# 使用  (?P=标签名)  来引用相同标签的分组，如果两者的内容相同则匹配成功，否则返回None
s1 = '<h1>wahahwahaha</h1>'
s2 = '<h1>wahahwahaha</h2>'
ret = re.search('<(?P<tag>\w+)>(?P<content>.*?)</(?P=tag)>',s1)
print(ret)   # <re.Match object; span=(0, 20), match='<h1>wahahwahaha</h1>'>

ret2 = re.search('<(?P<tag>\w+)>(?P<content>.*?)</(?P=tag)>',s2)
print(ret2)  # None

'''=================================取消分组优先显示 (?:) ======================================'''
ret = re.findall('\d+(\.\d+)?','12.34+5')
print(ret)  # ['.34', '']

ret = re.findall('\d+(?:\.\d+)?','12.34+5')
print(ret)  # ['12.34', '5']