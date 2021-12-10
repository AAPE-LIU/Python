'''根据字符串的形式去导入模块'''
import importlib
redis = importlib.import_module('utils.redis')  # 本来在导入模块的时候，就会把模块里面的内容执行一遍，所以这里会直接打印
# 因为redis模块本身的内容就是打印
# redis = importlib.import_module('utils.redis.funcc')  # No module named 'utils.redis.funcc'; 'utils.redis' is not a package
print(redis)  # <module 'utils.redis' from 'C:\\Users\\prominent\\Desktop\\老男孩python\\day14\\utils\\redis.py'>
mongo = importlib.import_module('utils.mongo')

func = getattr(redis,'func')
func()