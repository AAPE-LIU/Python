'''
首先json是一个特殊的字符串
长得像列表/字典/字符串/数字/真假的字符串

序列化：把一个列表/字典/元组，转换成json格式的这种行为叫做序列化
反序列化：把长得像json格式的字符串转换成列表或者字典这种行为叫做反序列化

json的格式要求 ：
json中的类型只能有这几种：int, str ,list ,dict, bool
最外层必须是列表或字典
在json中如果包含字符串必须是双引号：为什么呢？因为只有在python中字符串可以用单引号表示
其他的语言不可以

'''
import json
v = [12,3,{2:'A','b':'Excalibur'},['shdu','shud'],True]
js = json.dumps(v)  # 序列化：将python的值转化为json格式的字符串
print(js)

v2 = '["alex",123]'  # 这个是json格式吗？
# 是！！json格式是个字符串，除去最外层字符串格式，再下一层是容器类型，即list或者dict
v3 = json.loads(v2)  # 将json格式反序列化，将json转化为python的格式类型
print(v3)

# 集合不可以作为转json的数据类型
q