import xlrd,xlwt
def json_get(json, l_key, default):
    ret = json
    for k in l_key:
        if type(k) == int:
            if k < 0:
                return default
            if not (type(ret) == list):
                return default
            if len(ret) <= k:
                return default
        elif type(k) == str:
            # if not (type(ret) == dict):
            #     return default
            if not k in ret:
                return default
        else:
            return default
    return 1
wb = xlrd.open_workbook('用户行为日志0501-0512.xls')  # 读取工作簿
ws = wb.sheet_by_name('pro用户行为日志20210501-20210512')  # 读取工作表
nwb = xlwt.Workbook(encoding='utf-8')
nws = nwb.add_sheet('pro用户行为日志20210501-20210512')
nws.write(0, 0, 'uid')  # 创建表头
nws.write(0, 1, 'body')  # 创建表头
r = 0  # 设置循环变量
i = 0  # 设置行号变量
while r < ws.nrows-1:
    r += 1
    l = ws.row_values(r)
    if json_get(l[7], ['ct', 'l'], 0) == 1:
        i += 1  # 控制录入行号
        nws.write(i, 0, l[0])  # 录入要求数据
        nws.write(i, 1, l[7])  # 录入要求数据
nwb.save('用户行为日志4.xls')  # 保存录入的数据到指定文件夹
wb2 = xlrd.open_workbook('用户行为日志4.xls')  # 读取工作簿
ws2 = wb.sheet_by_name('pro用户行为日志20210501-20210512')  # 读取工作表
nwb1 = xlwt.Workbook(encoding='utf-8')
nws1 = nwb.add_sheet('用户行为日志20210501-20210512')
nws1.write(0, 0, 'uid')  # 创建表头
nws1.write(0, 1, 'body')  # 创建表头
r = 1
if r == 1:
# while r<ws2.nrows-1:
    l2 = ws2.row_values(r)
    str1_list = l2[7].split(',')
    print(str1_list)
    print(str1_list[0].split(':'))
    d = {}
    for l in str1_list:
        key,value = l.split(':')
        if key == 'ct' or key == 'l':
            d[key] = value
    nws1.write(r, 0, l2[0])  # 录入要求数据
    nws1.write(r, 1, d)  # 录入要求数据
nwb1.save('用户行为日志完全.xls')  # 保存录入的数据到指定文件夹

# nwb.save('用户行为日志4.xls')  # 保存录入的数据到指定文件夹
# print(type(l2))

