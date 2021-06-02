import openpyxl
wb = openpyxl.load_workbook('085400排名.xlsx')
ws = wb.active  # 获取当前活动表单
ws1 = wb.worksheets[0]  # 根据索引值获取工作表,worksheets相当于工作表集合
print(ws)
print(ws1)
ws2 = wb['Sheet3']  # 以工作表名获取工作表
print(ws2)
for shee in wb.worksheets:
    print(shee)  # 以循环方式获取工作表
print(wb.sheetnames)  # 获取所有的工作表名

wb.worksheets[2].title = 'zhidu'  # 修改工作表名
wb.save('085400排名.xlsx')
