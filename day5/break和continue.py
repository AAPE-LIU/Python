# 循环吃5个苹果，吃完第三个吃饱了，第四个和第五个不吃了（不执行）
# 循环吃5个苹果，吃第三个的时候吃出了虫子，第三个不吃了，吃第四个第五个
i = 0
while i < 5:
    i += 1
    if i == 3:
        print('吃饱了')
        break
print(f'吃了{i}个苹果', end='\n\n')

j = 0
while j < 5:
    j += 1
    if j == 3:
        print(f'第{j}个怎么有个虫子啊！！这个我不吃了')
        continue
    print(f'吃了第{j}个苹果')
# 下面这个例子将会使程序陷入死循环，因此有一个注意事项
j = 1
while j <= 5:
    if j == 3:
        print(f'第{j}个怎么有个虫子啊！！这个我不吃了')
        # 如果要使用continue，在continue之前一定要修改计数器，否则陷入死循环
        j += 1
        continue
    print(f'吃了第{j}个苹果')
    j += 1