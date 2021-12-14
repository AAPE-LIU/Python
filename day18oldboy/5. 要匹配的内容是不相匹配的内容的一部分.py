import re

# 我想匹配所有的整数
ret = re.findall(r'\d+','1-2(60+(-40.35/5)-(-4*3))')
print(ret)  # ['1', '2', '60', '40', '35', '5', '4', '3'] 这样会将40.35中的35也匹配进来

# 解决这种问题的方法就是把那个不想匹配的先匹配出来，然后删掉
ret2 = re.findall(r'\d+\.\d+|(\d+)','1-2(60+(-40.35/5)-(-4*3))')
ret2.remove('')
print(ret2)


'''re.方法中的参数
flags有很多可选值：
如果提前使用了compile那么flags就要在compile中设置了
re.I(IGNORECASE)忽略大小写，括号内是完整的写法
re.M(MULTILINE)多行模式，改变^和$的行为
re.S(DOTALL)点可以匹配任意字符，包括换行符
re.L(LOCALE)做本地化识别的匹配，表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境，不推荐使用
re.U(UNICODE) 使用\w \W \s \S \d \D使用取决于unicode定义的字符属性。在python3中默认使用该flag
re.X(VERBOSE)冗长模式，该模式下pattern字符串可以是多行的，忽略空白字符，并可以添加注释
'''
