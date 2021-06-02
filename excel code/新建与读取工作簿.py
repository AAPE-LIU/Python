# excel的新建，读取，保存
import openpyxl
wb = openpyxl.Workbook()  # W要大写
wb.save('我的工作簿.xlsx')  # 每个工作簿创建之后，会自行创建一个工作表
data = openpyxl.load_workbook('我的工作簿.xlsx')  # 读取工作簿
data.save('我的工作簿.xlsx')  # 如果工作簿处于打开状态，这样存储会出错
# 但是如果是关闭状态，或者存储的名字不完全一样了，则不会出错
