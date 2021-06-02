import openpyxl
wb = openpyxl.load_workbook('085400排名.xlsx')
print(wb.worksheets)
ws = wb.copy_worksheet(wb['Sheet1']).title = '复制品1'
wb.save('085400排名.xlsx')