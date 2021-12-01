def out(a):
    def wrapper(index):
        def inner(*args,**kwargs):
            data = index(*args,**kwargs)
            return data
        return inner
    return wrapper

@out(9)
def index():
    return 10
print(index())

# 写一个带参数的装饰器，实现：参数是多少，被装饰的函数就要执行多少次，把每次结果添加到
# 列表中，最终返回列表
def out(a):
    def wrapper(index):
        def inner(*args,**kwargs):
            list1 = []
            for i in range(a):
                data = index(*args,**kwargs)
                list1.append(data)
            return list1
        return inner
    return wrapper

@out(9)
def index():
    return 10
print(index())