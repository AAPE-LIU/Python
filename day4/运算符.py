# 算术运算符
c = 10
# 运行顺序是c += 3还是c = 10 + 1 + 2 ？
c += 1 + 2
print(c)

d = 10
d *= 1 + 2
print(d)
print(1 == 1)

# 逻辑运算符：
d = 0
a = 1
b = 2
c = 3
print((a < b) and (b < c))
print((a > b) or (b > c))
print(not b)
print(1 and 2)
print(0 and 1)
print(1 and 2 and 3 and 0)
print(0 or 0 or 1 or 0)
print(1 or 0 or 2)