money = int(input('口袋里有多少钱啊？'))
if money > 4:
    print(f'我有{money}块钱，可以坐公交')
    seat = int(input('有几个座位啊？'))
    if seat > 0:
        print(f'还有{seat}个座位，可以坐下')
    else:
        print(f'没有座位咯，那就站着吧')
else:
    print(f'我只有{money}块钱，坐不起公交车')