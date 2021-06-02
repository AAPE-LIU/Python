import openpyxl
wb = openpyxl.load_workbook('085400排名.xlsx')
# wb.remove(wb.worksheets[6])  # 可以用索引
# wb.remove(wb['Sheet1'])  # 也可以用名称
# wb.remove(wb.active)  # 也可以用活动表
wb.save('085400排名.xlsx')