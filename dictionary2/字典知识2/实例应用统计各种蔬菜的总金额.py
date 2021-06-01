import xlrd
wb = xlrd.open_workbook('工作簿1.xlsx')
ws = wb.sheet_by_name('Sheet1')
r = 0;d = {'ct':'', 'bright':''}
print(d)
while r<ws.nrows-1:
    r+=1
    item = ws.row_values(r)[5:6]
    if item[0] in d.keys():
        print(item)
