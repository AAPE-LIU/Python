import random
'''
1.出拳：
  玩家出拳
  电脑出拳
2.判断输赢
'''
player = int(input('请出拳：0--石头，1--剪刀，2--布'))
computer = random.randint(0, 2)
print(computer)
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜！哈哈哈')
elif computer == player:
    print('别跑！再来一把！')
else:
    print('电脑获胜')
# 上述代码暂时将电脑的出拳设置成了1，那么随机的数值该怎么设计呢？
# 引入模块，然后调用模块
'''
1.import导出模块：import random
2.模块名.模块功能：random.randint
'''