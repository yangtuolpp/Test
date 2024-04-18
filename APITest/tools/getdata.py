# getdata
# 2024/4/12
import json
import xlrd
from xlutils.copy import copy


def get_excel(sheet_name, castname):  # (表明，用例名称)
    rowlist = []
    # 表的路径
    excelpath = '../data/接口用例.xls'
    # 打开表，formatting保持表的样式
    workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # 打开文件
    # 获取指定的表
    worksheet = workbook.sheet_by_name(sheet_name)
    # 4读取单元格---返回的是字符串---cell(行号，列号)，从0开始
    # print(worksheet.cell(1,9).value())
    # print(worksheet.col_values(0))
    two = 0  # 开始的下标
    for one in worksheet.col_values(0):
        if castname in one:
            resBoydata = worksheet.cell(two, 9).value  # 请求数据
            data = worksheet.cell(two, 11).value  # 响应数
            rowlist.append((json.loads(resBoydata), json.loads(data)))  # str转字典
        two += 1
    return rowlist


def excelwrite():
    excelpath = '../data/接口用例.xls'
    workbook = xlrd.open_workbook(excelpath, formatting_info=True)  # 打开原表
    workbooknew = copy(workbook)  # 复制表
    worksheetnew = workbooknew.get_sheet(0)  # 获取表的第一个sheet，只能用下标
    return workbooknew, worksheetnew#复制出来的表以及第一个表


if __name__ == '__main__':
    # print(get_excel('登录', 'login'))
    excelwrite()
