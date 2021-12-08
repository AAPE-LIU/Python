'''发生异常的时候有各种因素引起的异常，其中Exception最为强大，可以捕获到各种异常
但是如果我们想直接定位异常的原因的话，可以更加细化地去划分异常的原因'''

# int('akjsdghfuj')  # ValueError: invalid literal for int() with base 10: 'akjsdghfuj'
# list1 = []
# list1[100]  # IndexError: list index out of range

# 下面这种是最简单的异常处理方法
try:
    list1 = []
    list1[100]  # # 其实这个是IndexError
except Exception as e:
    print('发生异常',e)  # 发生异常 list index out of range

try:
   int('akjsdghfuj')  # 其实这个是ValueError
except Exception as e:
    print(e)  # invalid literal for int() with base 10: 'akjsdghfuj'

'''上面两个一个是ValueError一个是IndexError，由于Exception功能太强大，都能捕获到
所以不会报错，但是也不会显示详细的报错信息，因此我们可以细化报错原因'''
# 可以使用下面这种结构，在前面先细化报错原因，如果前面没拦截到，最后让EXception把关
try:
   int('akjsdghfuj')  # 其实这个是ValueError
except ValueError as v:
    print('ValueError')
except IndexError as i:
    print('IndexError')
except Exception as e:
    print(e)  # invalid literal for int() with base 10: 'akjsdghfuj'

'''另外python中还有一种独有的方法finally方法，这种方法不管报不报错最后都会执行
即使finally写在return的后面，且函数已经return了，finally还是会执行'''
def func():
    try:
        int('123')
        return 123
    except ValueError as v:
        print('ValueError')
    except IndexError as i:
        print('IndexError')
    except Exception as e:
        print(e)  # invalid literal for int() with base 10: 'akjsdghfuj'
    finally:
        print('finally')
func()  # finally

'''==============================另外一种情况就是代码可以主动触发异常=========================='''
try:
    int(123)
    raise Exception('我很贱我就要触发异常')  # 这里面的参数些什么，e接收的就是什么
except Exception as e:
    print(e)  # 这里打印的就是什么
