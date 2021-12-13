import random
def redbag(money,num):
    money = money*100
    list1 = random.sample(range(1,money),num-1)
    list1.sort()
    list1.insert(0,0)
    list1.append(money)
    for i in range(len(list1)-1):
        print((list1[i+1]-list1[i])/100)
redbag(10,4)
