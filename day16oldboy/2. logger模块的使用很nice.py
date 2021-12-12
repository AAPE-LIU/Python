# logger对象的使用
    # 1. 创建一个logger对象
    # 2. 创建一个文件操作符
    # 3. 创建一个屏幕操作符
    # 创建对象的时候全部要用logging
    # 4. 给logger对象绑定  文件操作符
    # 5. 给logger对象绑定  屏幕操作符

    # 链接到logger的时候全部要用logger.addHandler
'''logger对象的优点：可以写入log文件的同时在屏幕上打印出来，可以支持中文'''
# 吸星大法
import logging

logger = logging.getLogger()  # 创建logger对象
fh = logging.FileHandler('log.log')  # 创建文件对象  默认mode='a',写入时不会将上次的内容清空
sh = logging.StreamHandler()  # 创建屏幕输出对象
fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')  # 创建格式对象


sh.setFormatter(fmt)  # 将sh设定成fmt格式
fh.setFormatter(fmt)  # 将fh设定成fmt格式

logger.addHandler(fh)  # 给logger对象绑定fh
logger.addHandler(sh)  # 给logger对象绑定sh
logger.error('你好啊')