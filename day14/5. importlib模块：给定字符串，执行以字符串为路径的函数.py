import importlib
path = 'utils.redis.func'

func_path1,func_path2 = path.rsplit('.',maxsplit=1)
path1 = importlib.import_module(func_path1)  # 不能精确查找到py文件中的方法或者是类
fun = getattr(path1,func_path2)
fun()