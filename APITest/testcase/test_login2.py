# loging
# 2024/4/12
import json
import pytest
from tools.getdata import excelwrite,get_excel
# 1-读取数据

# 2-关联请求
from lib.aipLib.login import Login
#datalist(请求数据，预期响应结果)，返回的是列表
class TestLogin2(Login):
    def test_login2(self):
        workbookNew, worksheetNew = excelwrite()  # 复制出来的文件对象，子表对象
        datalist = get_excel('登录', 'login')
        for i in range(0,len(datalist)):  # （请求参数boby,响应数据）
            resq = Login().login(datalist[i][0], False)  # 实际响应结果  返回的是字典格式
            # 实际结果和预期结果比较
            if resq['mes'] == json.load(datalist[i][1])['mes']:

                print('------------pass断言正确-----------')
              #   #列表.index(元素)==求出该元素的下标
                worksheetNew.write(i, 12, 'pass')
            else:
                print('------------fail断言失败---------')
                worksheetNew.write(i, 12, 'fail')  # (行号，列号，字符串内容)
        # 3-写结果
        workbookNew.save('../data/test.xls')#保存文件的路径
if __name__ == '__main__':

    pytest.main(['-s', 'testcase/test_login2.py'])
    # pytest.main(['test_login.py', '-s', '--alluredir', '../report/tmp'])