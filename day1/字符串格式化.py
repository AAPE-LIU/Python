name = input('输入你的姓名：')
age = input('请输入你的年龄：')
template = '%s是我的名字，%s岁了'% (name,age,)  #最后一个逗号，表示结束标志，有时候不加是对的，有时候不加是错的
# 现阶段统以都加上！！
# 字符串中的%代表占位，先把位置给占住，
print(template)

name2 = '刘小总'
template1 = '%s的手机电量还有100%%'% (name2,)  # 想在格式化字符串中输出%，就必须写两个%%，即使用转义字符都不好使
print(template1)
