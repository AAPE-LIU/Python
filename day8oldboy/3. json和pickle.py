'''
json，优点：所有语言通用；缺点：智能序列化基本的数据类型list/dict/int.....
picke，优点：几乎能序列化python中的所有东西除了socket对象；缺点：序列化出来的东西不可读，只有python认识
        序列化出来的东西，经过反序列化仍然可用
'''
import pickle
set1 = {1,2,3,4}
pickle1 = pickle.dumps(set1)
print(pickle1)  # b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00\x8f\x94(K\x01K\x02K\x03K\x04\x90.'
data1 = pickle.loads(pickle1)
print(data1)  # {1, 2, 3, 4}
print(type(data1))  # <class 'set'>


def f1():
    print('我被反序列化回来，我仍然可用')

pickle2 = pickle.dumps(f1)
print(pickle2)  # b'\x80\x04\x95\x13\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x02f1\x94\x93\x94.'
func1 = pickle.loads(pickle2)  # <function f1 at 0x000001E76648F040>
print(func1)
func1()  # 我被反序列化回来，我仍然可用

'''
pickle.dumps(要序列化的内容，要写入的文件)  要注意pickle，dump出来的内容是已经编码过之后的
            可以参考上面的内容，pickle序列化之后的内容以b开头，代表已经经过编码了，因此写入的时候
            不需要加encoding，因为pickle.dump（）会自动帮你编码，或者写wb，而不是w
'''
# set2 = {3,5,7,9,7}
# f = open('log2.txt',mode='w',encoding ='utf-8')
# pickle.dump(set2,f)  # write() argument must be str, not bytes 为什么会报这个错呢，因为open中的参数，就表示要以字符串形式写入
'''======================================'''
# set2 = {3,5,7,9,7}
# f = open('log2.txt',mode='wb',encoding ='utf-8')  # binary mode doesn't take an encoding argument
# pickle.dump(set2,f)
'''======================================'''
set2 = {3,5,7,9,7}
f = open('log2.txt',mode='wb')
pickle.dump(set2,f)
f.close()
f = open('log2.txt',mode='rb')  # 以二进制读取
data2 = pickle.load(f)
print(data2)  # {9, 3, 5, 7}
f.close()