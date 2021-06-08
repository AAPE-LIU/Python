import xlrd,xlwt
import json
import re

wb = xlrd.open_workbook('D:/DeskTop/用户行为日志0501-0512.xls')  # 读取工作簿
ws = wb.sheet_by_name('pro用户行为日志20210501-20210512')  # 读取工作表
nwb = xlwt.Workbook(encoding='utf-8')
nws = nwb.add_sheet('pro用户行为日志20210501-20210512')
nws.write(0, 0, 'uid')  # 创建表头
nws.write(0, 1, 'ct')  # 创建表头
nws.write(0, 2, 'l')  # 创建表头
r = 0  # 设置循环变量
i = 0  # 设置行号变量
j = 0  # 设置列号
while r < ws.nrows-1:
    r += 1
    l = ws.row_values(r)
    try:  # 如果是空的则跳过
        body = json.loads(l[7])  
    except:
        continue
    if "nodes" not in body:  # 里面是否存在"node"这个key
        continue
    context = body["nodes"]  # 取出所有字符
    context = re.sub('true','True',context)  # 替换不符合格式的字符串true和false
    context = re.sub('false','False',context)
    body = eval(context)  # 转换成List
    for b in body:
        if "params" in b:
            para = b["params"]
            if 'l' in para and 'ct' in para:
                i += 1  # 控制录入行号
                if i//65536 > 0: # 限制行高，excel最长65536行
                    i = 1
                    j += 3
                nws.write(i, j, str(b["id"]))  # 录入要求数据
                nws.write(i, j+1, str(para["ct"]))  # 录入要求数据
                nws.write(i, j+2, str(para["l"]))  # 录入要求数据
                
nwb.save('D:/DeskTop/用户行为日志5.xls')  # 保存录入的数据到指定文件夹

