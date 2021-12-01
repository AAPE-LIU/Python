import math

for i in range(1,1001):
    list1 = []
    for item in range(1,i):
        if i % item == 0:
            list1.append(item)
    mul = 1
    for x in list1:
        mul = mul * x
    if sum(list1)== i:
        print(i)

