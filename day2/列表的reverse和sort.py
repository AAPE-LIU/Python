list1 = [1,4,3,2,45,68,45,35,23]
list1.reverse()
print(list1)  # [23, 35, 45, 68, 45, 2, 3, 4, 1]
list1.sort(reverse=True)
print(list1)  # [68, 45, 45, 35, 23, 4, 3, 2, 1]
list1.sort(reverse=False)
print(list1)  # [1, 2, 3, 4, 23, 35, 45, 45, 68]
