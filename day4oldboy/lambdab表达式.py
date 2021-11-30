'''
语法规则：lambda 传入参数 ：返回值
'''
func = lambda a,b : 100
result = func(10,20)
print(result)

func2 = lambda a,b :a*b
result = func2(15,9)
print(result)

func3 = lambda *args,**kwargs :len(args) + len(kwargs)
result = func3(1,2,3,4,a = 4,b = 5,c = 6)
print(result)

DATA = 100
func5 = lambda a : a + DATA  # 由于lambada表达式是一行代码，不能自己定义变量，所以当函数内
# 执行的某些变量在本作用域没有的话，就要去父级找，再没有就去更上一级
result = func5(3)
print(result)

def func6():
    func7 = lambda a : DATA + a
    return func7(2)
print(func6())

user_List = []
func8 = lambda x:user_List.append(x)
result = func8('alex')
print(result)
print(user_List)