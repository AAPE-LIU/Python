import logging


file_1 = logging.FileHandler('log1.log',mode='a',encoding='utf-8')  # 创建出文件的名称，用来存储日志内容的
fmt = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s')
file_1.setFormatter(fmt)  # 把file_1的格式设置成fmt格式

logger = logging.Logger('xxxxxxx',level=20)  # 日志对象的名称，等级
logger.addHandler(file_1)

logger.error('你好')  # 因为我们是用logger来写日志的，所以要将文件对象加入到logger中