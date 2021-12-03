from datetime import datetime,timezone,timedelta
import time
print(datetime.now())  # 2021-11-30 11:20:43.036482
'''===================================='''
# 如果我现在只想要年月日，或者想换一种表达方式该怎么操作？
# 引入 .strftime() 相当于格式化输出
ctime = datetime.now().strftime('%Y-%m-%d')
print(ctime)
ctime2 = datetime.now().strftime('%H-%M-%S')  # 11-25-41  时分秒
print(ctime2)
ctime3 = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
print(ctime3)
'''
2021-11-30 11:25:41.002286
2021-11-30
11-25-41
'''


v1 = datetime.now()  # 获取当前的本地时间
print('当地标准时间',v1)
v2 = datetime.utcnow()  # 获取当前的伦敦标准时间,伦敦的标准时间是用utctime来表示
print('伦敦标准时间：',v2)

'''获取指定时区的时间：timezone(timedelta(hours=4))  获取东四区的时间  timezone和timedelta都需要导包'''
v3 = timezone(timedelta(hours=3))  # 指定东4区  timezone代表时区   timedelta代表时间差值
# 如果是西区，就用负的
v4 = datetime.now(v3)
print('东三区时间：',v4)

'''====================datetime转换成字符串   strftime()======================'''
ctime1 = datetime.now()
print(ctime1,type(ctime1))  # 2021-11-30 14:34:59.008015 <class 'datetime.datetime'>
strtime = ctime1.strftime('%Y/%m/%d  %H/%M/%S')
print(strtime,type(strtime))  # 2021/11/30  14/34/59 <class 'str'>

'''======================字符串转换成datetime   strptime(要转换的字符串，要转换成的时间格式)======================'''
ctime2 = datetime.strptime('2025-4-25','%Y-%m-%d')
print(ctime2,type(ctime2))  # 2025-04-25 00:00:00 <class 'datetime.datetime'>

'''======================datetime的加减======================================'''
ctime1 = datetime.strptime('2021-12-01','%Y-%m-%d')
time2 = timedelta(days=26)
ctime2 = ctime1 + time2
print(ctime2)

'''========================时间戳和datetime的关系============================'''
# 时间戳转换为datetime类型
time1 = time.time()
ctime1 = datetime.fromtimestamp(time1)  # 代表从时间戳读入参数
print(ctime1,type(ctime1))

# datetime转换为时间戳类型
time2 = datetime.now()
time3 = time2.timestamp()
print(time3,type(time3))