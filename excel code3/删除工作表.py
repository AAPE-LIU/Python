import openpyxl
wb = openpyxl.load_workbook('批量建立的工作表.xlsx')
for sh in wb.worksheets:
    # print(sh.title.split('-')[0]!='北京')
    if sh.title.split('-')[0]!='北京':
        wb.remove(sh)
wb.save('批量建立的工作表.xlsx')