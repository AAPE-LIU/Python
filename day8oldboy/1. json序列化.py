'''如果字典中出现了中文，json序列化的时候会出现什么'''
import json
dict1 = {'name': 'Alex','age':20}
json1 = json.dumps(dict1)
print(json1)
dict2 = {'name':'刘总'}
json2 = json.dumps(dict2)
print(json2)  # {"name": "\u5218\u603b"}  这是个什么鬼啊？
# Unicode编码表
'''
如果我想让他正常显示该怎么办？
'''
json2 = json.dumps(dict2,ensure_ascii=False)  # 只需要将这个参数设置为False即可
print(json2)  # {"name": "刘总"}


