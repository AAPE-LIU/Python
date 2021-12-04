import requests
url_list = ['http://www.baidu.com', 'http://www.google.com', 'http://www.bing.com','http://www.bing.com']
# try位置不同所起到的作用也是不同的，比如func1中，只要循环内部有一次异常，整个循环终止，列表得不到完全遍历
def func1():
    content_list = []
    try:
        for i in url_list:
            ret = requests.get(i)
            content = ret.text
            content_list.append(content)
    except Exception as e:
        print('异常错误')
    return content_list
print(func1())
print('============================================================================================================')

# 在func2中try位置发生改变，可以使得列表完全遍历，最后再结束
def func2():
    content_list = []
    for i in url_list:
        try:
            ret = requests.get(i)
            content = ret.text
            content_list.append(content)
        except Exception as e:
            print('异常错误')
    return content_list
print(func2())