import requests
try:  # 尝试去做下面的内容，如果有错误，程序别报错，让我定义的异常处理来做
    val = 'asjdgfjas'
    num = int(val)
except Exception as e:
    print('操作异常')

'''========================异常处理就和if  else一样可以放在任何地方======================='''
try:
    ret = requests.get('http://www.baidu.com')
    print(ret.text)  # <!DOCTYPE html>
except Exception as e:
    print('请求异常')
print('===========================================================')
try:
    ret = requests.get('http://www.google.com')
    print(ret.text)
except Exception as e:
    print('请求异常')