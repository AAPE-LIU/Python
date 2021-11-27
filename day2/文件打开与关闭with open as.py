'''
文件打开时，一定哟啊记得关闭，否则会有内寸泄露的危险
但是平常我们经常会忘记close,因此又衍生出了一种可以自动关闭的写法
'''

# 文艺青年写法：需手动关闭
f = open('log.txt',mode='a',encoding='utf-8')
f.close()

# 二逼写法：自动关闭
with open('log.txt',mode='a',encoding='utf-8') as rf:
    data = rf.read()
    # 缩进内的代码执行完之后，会自动关闭文件