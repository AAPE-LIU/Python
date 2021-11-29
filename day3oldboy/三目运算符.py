'''
前面 if 条件 else 后面
当if条件满足的时候，值就取前面，否则就取后面
'''
# 判断输入的内容是否是数字，如果是的话就转换成数字，接收并且打印
data = input('请输入：')
data2 = int(data) if data.isdecimal() else None
print(data2)