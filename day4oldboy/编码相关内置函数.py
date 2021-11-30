'''
chr() ,将十进制数字转换为其对应的Unicode字符，Unicode包含ASCII值
ord() ，将Unicode编码转换成相应的十进制数字
'''
print(chr(10086))
print(chr(12315))
print(chr(91016))
num = ord('❦')
print(num)
str1 = '我爱中国'
for i in str1:
    num = ord(i)
    print(num)

'''
应用场景：
生成随机验证码，可以用random随机数字，然后将数字转换为字母，或者其他东东
'''
import random
str2 = ''
for i in range(4):
    num = random.randint(65,90)
    str2 = str2 + chr(num)
print(str2)
str1 = input('请输入屏幕上所出现的字母，不区分大小写：').upper()
if str1 == str2:
    print('您输入的验证码正确')
else:
    print('您输入的验证码有误')

