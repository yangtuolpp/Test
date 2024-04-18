# conftest
# 2024/4/13
# 环境初始化与清除操作
# 具有作用域，放在哪个包只对哪个包起作用！！！！！！！命名是固定写法conftest

import pytest
from lib.aipLib.login import Login
from lib.aipLib.myshop import myshop
from config.config import username

'''
scope代表fixture作用
function 默认，再conftest作用域下的所有def test_XX方法运行前都会执行
class  再conftest作用域下，每个TestXXX测试类运行前都会执行一次
module 再conftest作用域下，每个test__XX 测试模块，运行前都会执行一次！
session  再conftest作用域下，这个包  运行前都会运行  
'''


@pytest.fixture(scope='session', autouse=True)  # auto use自动调用，默认False，建议手动调用
def start_demo(request):  # 这是一个运行改包下，任何一个test文件，都会一开始执行的操作
    print('--开始执行自动化测试')

    yield  # 清除数据操作
    print('----自动化测试结束')


'''
fixture用法
1、使用函数名直接调用，但是没有返回值
@pytest.mark.usefixtures('update_init')#写入函数名
2、需要使用fixture的返回值时
直接再对应的接口函数中，加入一个形参，参数名就是fixture的名字

'''

'''
问题点：
1、店铺更新接口，每次操作都需要要登录，----繁琐
2、登录操作-其他模块也需要
3、如果业务比较复杂，需要前置条件进行模块化
'''
'''
解决方案：
1、将登录操作单独剥离出来
2、店铺的实例化单独玻璃出来
3、操作一个模块的测试，只需要登录一次
'''


# 1-将登录剥离出来
@pytest.fixture(scope='class')
def Login_init():
    token = Login().login(username, gettoken=True)
    return token


# 2-店铺实例化 -但是需要关联token的fixture
@pytest.fixture(scope='class')
def myshop_init(Login_init):
    # 在下一个fixture中需要fixture的返回值，可以将上一个fixture当作形参去调用
    shop = myshop(Login_init)
    return shop


# 3-店铺更新前的前置操作
@pytest.fixture(scope='function')
def update_init(myshop_init):  # 更新商铺的环境初始化
    shopid = myshop_init.shoplist({'page': 1, 'limt': 10})['data']['records'][0]['id']
    # 4-文件上传，获取图片信息
    imagepath = myshop_init.updata('123.png', '../data/123.png')
    return shopid, imagepath  # 元组类型，
    # 元组类型不能使用usefixtrue直接使用；可以放在函数参数中调用环境初始化方法名直接调用
