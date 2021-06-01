import xlrd,xlwt
wb = xlrd.open_workbook('用户行为日志0501-0512.xls')  # 读取工作簿
ws = wb.sheet_by_name('miot用户行为日志20210501-20210512')  # 读取工作表
nwb = xlwt.Workbook(encoding='utf-8')
nws = nwb.add_sheet('miot用户行为日志20210501-20210512')
nws.write(0, 0, 'uid')  # 创建表头
nws.write(0, 1, 'key')  # 创建表头
nws.write(0, 2, 'value')  # 创建表头
r = 0  # 设置循环变量
i = 0  # 设置行号变量
d = {'ct': '', 'bright': ''}  # 创建一个包含关键字的字典用来判断行数据是否符合
while r < ws.nrows-1:
    r += 1
    l = ws.row_values(r)  # 将每一行的数据读取出来
    if l[5] in d.keys():
        i += 1  # 控制录入行号
        nws.write(i, 0, l[0])  # 录入要求数据
        nws.write(i, 1, l[5])  # 录入要求数据
        nws.write(i, 2, l[6])  # 录入要求数据
nwb.save('用户行为日志3.xls')  # 保存录入的数据到指定文件夹