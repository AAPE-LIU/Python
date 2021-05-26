# 字符串操作之删除空白符
# lstrip():删除字符串左侧空白字符
# rstrip():删除字符串右侧空白字符
# strip():删除两侧空白字符
mystr = '''  big big city beauty duo      '''
new_str = mystr.lstrip()
print(new_str)

new_str2 = mystr.rstrip()
print(new_str2)

new_str3 = mystr.strip()
print(new_str3)