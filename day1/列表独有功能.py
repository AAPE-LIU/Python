'''
1.append()
2.insert()
3.remove()
4.pop()
'''
user = []
for i in range(3) :
    content = input("请输入你的姓名：")
    user.append(content)
    print(user)
print('===========================')
user.insert(2,'刘秀达')  # 插入位置，以及插入内容
print(user)
print('==========================')
user.remove('liudaidai')  # 如果内容不存在会报错,并且只会删除第一个检索到的
print(user)
print('============================')
user.pop(1)  # pop如果指定了删除位置的下标，就会按照下标去删除，否则默认删除最后一个
print(user)
'''
总结：
增：append()  insert()
删：remove()  pop()  del()
改：直接用索引改就可以
查：直接用索引查就可以
'''
'''
del和pop的区别，del删除元素就仅仅是删除而已，而pop删除元素，还会将删除的那个元素的
值返回给一个变量，接不接收都可以
'''
