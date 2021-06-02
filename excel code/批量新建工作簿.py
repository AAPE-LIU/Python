import openpyxl
for m in range(1, 13):
    wb = openpyxl.Workbook()
    # print('%d月.xlsx' % m)
    wb.save('%d月.xlsx' % m)