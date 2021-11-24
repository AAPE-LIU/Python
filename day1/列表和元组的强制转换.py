# 可迭代对象强制转换为列表
str1 = 'klasjhdfgokusadh'
list1 = list(str1)
print(list1)  # ['k', 'l', 'a', 's', 'j', 'h', 'd', 'f', 'g', 'o', 'k', 'u', 's', 'a', 'd', 'h']
# 上面那个没什么意义
# 但是对于元组转换为列表，还是有一些作用的
list2 = list((1,2,3,4,5,6))
print(list2)  # [1, 2, 3, 4, 5, 6]

# 元组的强制转换与列表一模一样

'''
nums = [11,22,33,44]
将11，22，33，44用下划线连接起来
'''
nums = [11,22,33,44]
for i in range(len(nums)):
    nums[i] = str(nums[i])
nums2 = '_'.join(nums)
print(nums2)
