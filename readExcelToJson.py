import os
import getpathInfo# 自己定义的内部类，该类返回项目的绝对路径
#调用读Excel的第三方库xlrd
from xlrd import open_workbook
import json
import tablib
# 拿到该项目所在的绝对路径
path = getpathInfo.get_Path()

class readExcel():
    def get_xls(self, xls_name, sheet_name):# xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, "testFile", 'case', xls_name)
        file = open_workbook(xlsPath)# 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)#获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):#根据行数做循环
            if sheet.row_values(i)[1] != u'event':#如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
                cls.append(sheet.row_values(i))
        return cls

    def set_xls(self,xlsPath, rows):

        header = tuple([i for i in rows[0].keys()])
        data = []
        # 循环里面的字典，将value作为数据写入进去
        for row in rows:
            body = []
            for v in row.values():
                body.append(v)
            data.append(tuple(body))

        data = tablib.Dataset(*data, headers=header)

        open(xlsPath, 'wb').write(data.xlsx)

if __name__ == '__main__':#我们执行该文件测试一下是否可以正确获取Excel中的值

    all=readExcel().get_xls('RealU208.xlsx', 'register_result')
    alldata=[]
    for i in range(len(all)):
        alldata.append(json.loads(all[i][2]))
    print(alldata)
    readExcel().set_xls('./testFile/case/data.xlsx',alldata)

    # with open('./json.txt', 'r') as f:
    #     rows = json.load(f)
    # 将json中的key作为header, 也可以自定义header（列名）
    # print(rows)
    # header = tuple([i for i in rows[0].keys()])
    #
    # data = []
    # # 循环里面的字典，将value作为数据写入进去
    # for row in rows:
    #     body = []
    #     for v in row.values():
    #         body.append(v)
    #     data.append(tuple(body))
    #
    # data = tablib.Dataset(*data, headers=header)
    #
    # open('./testFile/case/query_result_2021-06-01.xls', 'wb').write(data.xls)
