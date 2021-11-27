'''
让用户一直输入账户和密码，直到用户输入N
以列表存储字典的形式存储
user_list = [
{'user':'用户输入','pwd':'用户输入'},
{'user':'用户输入','pwd':'用户输入'},
{'user':'用户输入','pwd':'用户输入'},
{'user':'用户输入','pwd':'用户输入'},
{'user':'用户输入','pwd':'用户输入'}]
'''
list = []
while True :
    dict = {}
    user_id = input('请输入您的用户名：')
    if user_id == 'N':
        break
    password_id = input('请输入您的密码：')
    dict['user'] = user_id
    dict['pwd'] = password_id
    list.append(dict)
print(list)