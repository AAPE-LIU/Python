'''应用场景：将异常处理捕获到的内容，使用日志模块将其保留到日志文件'''
import logging
logging.basicConfig(filename='cmdb.log',level=20)

logging.log(10,'sjhdgfjshd')
logging.log(20,'yyyyyyyyy')
logging.log(30,'jjjjjjjjjjjjjj')
# 为什么并没有将第一个写进去呢？因为他没达到设置的严重级别,大于等于严重级别都可以写入log日志
# 在logging文件中有如下的级别规定，这也对应于写出来的log文件中内容前的标志
'''
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''
# 其实不需要像上面那样手动去设定级别，因为在logging模块中有对应的方法和上面的
# 严重等级是一一对应的，只不过是小写
logging.debug('debugdebugdebugdebug')
logging.critical('criticalcriticalcriticalcritical')
logging.warning('warningwarningwarningwarning')

'''===============================那么如何使用呢？======================================'''
try:
    pass
except Exception as e:  # 要将e转换成字符串才可以写入logging日志文件中
    msg = str(e)  # 执行e.__str__方法
    logging.error(msg)
