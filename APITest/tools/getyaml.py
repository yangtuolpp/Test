# getyaml
# 2024/4/13
import json

import yaml
def getyaml_data(filedir):
    # 1-打开文件
    fo = open(filedir, 'r')
    # 2-使用第三方库去获取
    res = yaml.safe_load(fo)
    # print(res['info2'])
# def getyaml_data(filedir):
#     '''
#     原则：少动代码，代码和数据做分离
#     思路：获取什么数据；取传参和返回数据，data\resp
#     2、数据如何封装返回
#         分析：
#         1、pytest需要什么数据；（需要列表格式（indata））[(),()]
#         2、要求字典格式
#             回顾：以前读取excel数据的时候，在excel做了load
#             json----转化----字典
#     '''
#     # 1-打开文件
#     reslist = []
#     fo = open(filedir, 'r')
#     # 2-使用第三方库去获取
#     # 文件里面包含多个yaml
#     res = yaml.safe_load_all(fo)
#     print(type(res))
#     # 需要用循环来打印
#     # for one in res:
#     #     reslist.append((one['data'], one['resp']))
#     # return  reslist
#
#
# if __name__ == '__main__':
#     print(getyaml_data('../config/conf.yaml'))


def getyaml_data2(filedir):
    '''
    原则：少动代码，代码和数据做分离
    思路：获取什么数据；取传参和返回数据，data\resp
    2、数据如何封装返回
        分析：
        1、pytest需要什么数据；（需要列表格式（indata））[(),()]
        2、要求字典格式
            回顾：以前读取excel数据的时候，在excel做了load
            json----转化----字典
    '''
    # 1-打开文件
    reslist = []
    fo = open(filedir, 'r')
    # 2-使用第三方库去获取
    # 文件里面包含多个yaml
    res = yaml.safe_load_all(fo)
    # 需要用循环来打印
    for one in res:
        reslist.append((one['data'], one['resp']))
    return  reslist


if __name__ == '__main__':
    print(getyaml_data2('../data/data.yaml'))
