# 字符串类型
# 单引号可以用来表示字符串
a = 'hello world'
b = 'hello ' \
    'world'
print(type(a))
print(a)
print(b)

# 双引号也可以用来表示字符串
f = "good"
print(type(f))

# 三引号也可以用来表示字符串
c = '''my name is liuxiuda'''
d = """zuihou
yibeijiu"""
print(type(c))
print(type(d))
print(c)
print(d)
# 区别：三引号支持回车换行操作，并且回车换行之后不会添加任何其他的字符
#       并且输出的结果也是换行的，而单引双引则不同

# 在字符串中键入单引号或者双引号该怎么做
# 例如我想输出I'm Tom
# 将字符串标志改为双引，依情况而定也可以改为单引达到效果
e = "I'm Tom"
print(e)
# python中要求单引或者双引要成对出现
# 多出来的那个可以用转义字符将他转义
g = 'I\'m Tom'
print(g)

# 巩固字符串输出
name = '秀达'
print('我的名字是%s' % name)
print(f'我的名字是{name}')
