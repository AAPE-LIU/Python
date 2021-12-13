# eval() 将字符串类型的代码执行并返回结果
print(eval('1+2+3+4'))
# exec()将自字符串类型的代码执行
print(exec("1+2+3+4"))  # None
exec("1+2+3+4")  # 10
exec("print('hello,world')")  # hello,world

'''
参数说明：　　　

1. 参数source：字符串或者AST（Abstract Syntax Trees）对象。即需要动态执行的代码段。　　

2. 参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
    当传入了source参数时，filename参数传入空字符即可。　　

3. 参数model：指定编译代码的种类，可以指定为 ‘exec’,’eval’,’single’。
    当source中包含流程语句时，model应指定为‘exec’；
    当source中只包含一个简单的求值表达式，model应指定为‘eval’；
    当source中包含了交互式命令语句，model应指定为'single'。
'''
#流程语句使用exec
code1 = 'for i in range(0,10): print (i)'
compile1 = compile(code1,'','exec')
exec (compile1)

 #简单求值表达式用eval
code2 = '1 + 2 + 3 + 4'
compile2 = compile(code2,'','eval')
print(eval(compile2))

#交互语句用single
code3 = 'name = input("please input your name:")'
compile3 = compile(code3,'','single')
print(exec(compile3))
print(name)
a = '12.756'
print(eval(a),type(eval(a)))