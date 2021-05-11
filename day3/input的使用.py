'''
input('提示信息')
在python中input接收用户的输入后，一般存储到变量，方便使用
在python中，input会把接收到的任意用户输入的数据都当做字符串处理
'''
password = input('请输入您的密码：')
print(f'您输入的密码是：{password}')
print('type(password)')
print(type(password))