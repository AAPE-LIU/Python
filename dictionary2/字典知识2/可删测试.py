import xlrd
wb = xlrd.open_workbook('222.xls')  # 读取工作簿
ws = wb.sheet_by_name('Sheet1')  # 读取工作表
data = ws.row_values(1)
print(type(data))