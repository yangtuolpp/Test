# getexcel
# 2024/4/12
import xlrd
import xlutils
from xlutils.copy import copy


def get_excel(sheet_name, start_row, end_row):
    rowlist = []
    # 表的路径
    excelpath = '../data/接口用例.xls'
    # 打开表，formatting保持表的样式
    workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # 打开文件
    # 获取文件所有的sheet 表名
    # wooksheet = workbook.sheet_names()
    # 3获取某一个指定的sheet
    worksheet = workbook.sheet_by_name(sheet_name)
    # 4读取单元格---返回的是字符串---cell(行号，列号)，从0开始
    for one in range(start_row - 1, end_row):
        resqBodydata = worksheet.cell(one, 9).value  # 请求数据
        respData = worksheet.cell(one, 11).value  # 响应参数
        rowlist.append((resqBodydata, respData))
    return rowlist


def copyexceldata():
    rowlist = []
    # 表的路径
    excelpath = '../data/接口用例.xls'

    # 打开表，formatting保持表的样式
    workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # 打开文件
    workbookNew = copy(workbook)#copy表
    worksheetNew = workbookNew.get_sheet(0)
    return workbookNew,worksheetNew

if __name__ == '__main__':
    data=get_excel('登录',1+1,3)
    print(data)
    print(len(data))
    for i in range(0,2):
        print(data[i][0])

    # for i in get_excel('登录', 2, 7):
    #     print(i)
    #     print(len(i))
