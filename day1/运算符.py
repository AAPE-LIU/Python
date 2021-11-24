# 字符串转数字
# 直接用int包裹就可以，但是前提是字符串中的内容要是int
# int转字符串也是直接用str包裹就可以
# 那么数字和字符串转bool值得规律是什么呢？
# 只有当数字为0以及当str为空的 时候bool值为false，其他全为true
value = 1 or 9
print(value)  # 1
value2 = 0 or 9
print(value2) # 9
print(bool(value2))
'''
如果又有and又有or，该怎么办？这里面有一个优先级，先算and再算or
运算符优先级关系：() > not > and > or
大于小于号的运算优先级高于or
'''
value3 = 1 and 9 or 0 and 6
# 首先 1 and 9 值为9 ，有了9，后面还有个or，所以后面就不用看了，整个式子为9
