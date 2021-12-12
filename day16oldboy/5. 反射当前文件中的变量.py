import sys

ab = 'liuzong'
path = getattr(sys.modules[__name__],'ab')  # 最好能背下来
print(path)

print(sys.modules[__name__])

# 当在当前文件中执行的时候__name__ = __main__,如果是由其他模块调用的话，__name__ 的值为他所在的模块的名称
