# 第一步：执行ret = xxx(index)
# 第二步：执行index = ret
@xxx
def index():
    pass

# 带参数的装饰器：
# 第一步：执行v = uuu(9)
# 第二步：执行ret = v(index)
# 第三步：index = ret
# 就相当于多执行了一步，带参数的装饰器是先将uuu(9)执行过之后，才能生成相当于xxx的东西
@uuu(9)
def index():
    pass
