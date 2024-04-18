# test_login
# 2024/4/12
# 1封装测试类
import pytest
from lib.aipLib.login import Login
from tools.getdata import get_excel
import json,os
class TestLogin():
    # [({},{}),({},{})]
    @pytest.mark.parametrize('indata,respdata', get_excel('登录', 'login'))  # ('变量',值)
    def test_login(self, indata, respdata):
        res = Login().login(indata, gettoken=False)
        # 参数化，从excel中读取输入和输出结果进行断言
        assert res['mes'] == respdata['mes']

if __name__ == '__main__':
    for one in os.listdir("../report"):
        if 'txt' in one:
            os.remove(os.path.join("../report", one))

    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
#方案二,自动打开浏览器
# os.system('allure serve ../report/tmp')
'''
修改验证代码
'''