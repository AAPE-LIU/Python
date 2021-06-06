import xlwt
# 1.创建工作簿
wb = xlwt.Workbook()
# 2.创建工作表
ws = wb.add_sheet('moit用户行为日志20210501-20210512')

# 3.填充数据
ws.write_merge(0, 1, 0, 8, '第一次处理数据')
# 写入数据
data = (('uid',	'did',	'model',	'p_type',	'type',	'key',	'value',	'time',	'dt'
), (11861261,	270297834,	'yeelink.light.ceiling21',	'up_event',	'prop',	'nl_br',	'[0]',	1619883277,	'2021/5/1'
), (11861261,	270297834,	'yeelink.light.ceiling21',	'up_event',	'prop',	'active_bright',	'[100]',	1619883275,	'2021/5/1')
)
for i, item in enumerate(data):
    for j, val in enumerate(item):
        ws.write(i+2, j, val)
# 创建第二个工作表
ws2 = wb.add_sheet('pro用户行为日志20210501-20210512')
# 写入图片
# ws2.insert_bitmap('123.bmp', 0, 0)
# 4.保存
wb.save("2021数据处理.xls")