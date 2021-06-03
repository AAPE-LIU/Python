import openpyxl
# 批量建立工作表
wb = openpyxl.Workbook()
for shee in range(1, 13):
    wb.create_sheet('%d月' % shee)
wb.remove(wb['Sheet'])
wb.save('批量建立的工作表.xlsx')

