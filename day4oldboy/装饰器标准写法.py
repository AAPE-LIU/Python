def wrapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

# 为什么要加参数呢？不加不行么
# 有如下情况
@wrapper
def func1():
    print(123)

@wrapper
def func2(a):
    print(a+100)
func1()
func2(10)