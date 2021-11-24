# code = "DigiTal"
# while True :
#     check_code = input("请输入你的验证码：%s" % code)
#     if code.lower() == check_code.lower() :
#         print('验证码正确')
#         break
#     else :
#         print("验证码错误请重新输入")
#
while True:
    serve = input('''请输入你要进行的服务
    1.吃饭
    2.人工客服
    3.客服评价
    4.话费查询''')
    if serve.isdigit() :
        print('输入正确，正在为你转接')
        break
    else :
        print('输入有误，请重新输入')