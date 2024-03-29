# 字典的应用场景
# 思考1：如果有多个数据，例如：'Tom', '男', 20,如何快速存储？
# 答：列表
# list1 = ['Tom', '男', 20]
# 思考2：如何查找到数据'Tom'？
# 查找下标为0的数据即可
# list1[0]
# 思考3 如果将来数据顺序发生变化，如下所示，还能用list[0]访问到数据
# 'Tom'吗？
# list1 = ['男', 20, 'Tom']
# 答：不能，数据'Tom'此时下标为2
# 思考4：数据顺序发生变化，每个数据的下标也会发生变化，如何保证数据顺序
# 变化前后能使用同一的标准查找数据呢？
# 答：字典，字典里面的数据都是以键值对的形式出现的，字典数据和数据顺序没有
# 关系，即字典不支持下标，后期数据无论如何变化，只需要按照对应的键的名字查找数据即可
