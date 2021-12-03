'''
json.dump(字典，要写入的文件)
将字典序列化之后写入到一个文件中去，因此传参的时候要传入一个要序列化的字典和一个文件
'''
import json
dict2 = {'name':'刘总'}
f = open('log.txt',mode='w',encoding='utf-8')  # 如果不写mode='w'并且你还没有这个文件，他会报错
json.dump(dict2,f,ensure_ascii=False)  # 序列化之后写进一个文件中，你写入文件你得先打开文件，因此要先执行open操作

'''
json.load(打开的文件)
将文件中的内容读取并且转换成字典
'''
f = open('log.txt',mode='r',encoding='utf-8')
data = json.load(f)
print(data)