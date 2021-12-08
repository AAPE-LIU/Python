'''
网站的底层就是这样
'''
from wsgiref.simple_server import make_server

def func(environ,start_response):
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return ['刘总'.encode("utf-8")]

class Foo():
    def __call__(self,environ,start_response):
        start_response("200 OK", [('Content-Type', 'text/html; charset=utf-8')])  # 渲染网页将plain改为了html
        return ['刘<h2 style=color:red>xiao总</h2>'.encode("utf-8")]

'''函数执行方法'''
# server = make_server('127.0.0.1',8000,func)  # 一个ip一个地址，只要有人访问这个网站的地址，就会自动找到第三个参数
                                            # 给他加括号并且执行
obj = Foo()
server = make_server('127.0.0.1',8000,obj) # 一个ip一个地址，只要有人访问这个网站的地址，就会自动找到第三个参数
                                 # 给他加括号并且执行,由于这里第三个参数是一个对象，因此加了括号会执行__call__方法
server.serve_forever()