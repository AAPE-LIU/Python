import xlrd
# 1.找到想要读取的excel文件
# 用xlrd提供的open_workbook来读取excel文件，这个函数返回的是一个工作簿的对象，用wb来接收
wb = xlrd.open_workbook("用户行为日志0501-0512.xlsx")
# 安装了xlrd直接运行会报错，这时需要下载pip install pyexcel-xls
# print(wb.sheet_loaded(0))  # 查看索引为0的工作表当前是否被加载，括号内可以是工作表的名称或者索引
# wb.unload_sheet(0)  # 卸载已经加载的索引为0的工作表
# print(wb.sheet_loaded(0))  # 再次查看索引为0的工作表是否被加载

# print(wb.sheets())  # 获取全部sheet
# print(wb.sheets()[0])  # 获取某一个工作表
# print(wb.sheet_by_index(0))  # 根据索引获取某一工作表
# print(wb.sheet_names())  # 获取所有工作表的名字
# print(wb.sheet_by_name('miot用户行为日志20210501-20210512'))  # 根据名字获取工作表
# print(wb.nsheets)  # 返回excel工作表的数量

# 操作excel行
sheet = wb.sheet_by_index(0)
print(sheet.nrows)  # 获取sheet下的有效行数
print(sheet.row(1))  # 该行单元格对象组成的列表
print(sheet.row_types(1))  # 获取单元格的数据类型--输出结果array('B', [2, 2, 1, 1, 1, 1, 1, 2, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0])
# 其中1表示字符串，2表示num，3表示data，4表示bool，5表示error
print(sheet.row(2)[4])  # 目前获取的还只是单元格的对象，还带着数据类型text
# 如果只想要获取单元格内容，其他的不要该怎么做呢
print(sheet.row(2)[4].value)  # 这样就只会获取数据而不会夹杂其他东西
# 上述代码只是获取一行中某个单元格的数据，如果想要获取整行数据呢？
# 可以使用函数row_values函数
print(sheet.row_values(2))
print(sheet.row_len(2))  # 得到单元格的长度


# 操作excel列
sheet2 = wb.sheet_by_index(0)
print(sheet2.ncols)  # 获取有效列数
# print(sheet2.col(1))  # 获取该列单元格对象组成的列表
print(sheet2.col(5)[3].value)
# print(sheet2.col_values())  # 打印本列所有元素



# 操作excel单元格
print(sheet.cell(2, 3))  # 返回的是对象，并非是一个纯数据
print(sheet.cell(2, 3).value)
print(sheet.cell_type(2, 3))