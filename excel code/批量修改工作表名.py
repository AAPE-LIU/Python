import openpyxl
wb = openpyxl.load_workbook('085400排名.xlsx')
for sh in wb.worksheets:
    print(sh.title+'只读？')
    sh.title = sh.title+'只读？'
    wb.save('085400排名2.xlsx')