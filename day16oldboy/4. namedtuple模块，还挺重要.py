from collections import namedtuple
Course = namedtuple('Cour',['name','price','age'])  # 可命名元组
# 上一步相当于创建了一个类，这个类没有方法，所有的属性值都不能修改
msg = Course('刘总',1000000000,22)  # 这一步相当于创建了一个对象，给类中的变量赋了初始值
print(msg)  # Cour(name='刘总', price=1000000000, age=22)