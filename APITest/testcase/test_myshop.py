# test_myshop
# 2024/4/12
import pytest
from lib.aipLib.login import Login
from lib.aipLib.myshop import myshop
from tools.getdata import get_excel
from config.config import username
@pytest.mark.shop#给用例加标签，可以选择性的某一类标签的运行
class TestMyShop():
    def setup_class(self):
        #所有实例，只需登录一次，可以使用参数化---配置文件实现;
        #在config中将用户名和密码参数化【username】做调用，后续更改的话方便
        self.token = Login().login(username, gettoken=True)
        #每次都要创建店铺实例，所以可以再前置初始化中创建实例，下面使用时调用即可
        self.myshop = myshop(self.token)
    #列出店铺

    @pytest.mark.shop_list#给用例加标签，可以选择性的某一类标签的运行
    @pytest.mark.parametrize('indata,resdata', get_excel('我的商铺', 'listshopping'))
    def test_myshoplist(self, indata, resdata):
        res = self.myshop.shoplist(indata)
        if 'code' in res:
            assert res['code'] == resdata['code']
        else:
            assert res['error'] == resdata['error']

    #2-更新店铺
    #在执行店铺更新的接口时不光需要登录操作，还有一些前置操作比如上传文件
    #只有更新店铺的接口需要，其他接口不需要，那就不能放在setup中
    #fixture环境初始化与清除操作！！！！！！！！与setup和teardown不一样
    #fixture可以再某个特定的用例中运行，只需要调用即可，比setup和teardown方便
    @pytest.mark.update#给用例加标签，可以选择性的某一类标签的运行
    #无条件跳过
    @pytest.mark.skip(reason='不执行跳过')#无条件跳过
    #有条跳过
    @pytest.mark.skipif(1==2,reason='如果条件满足，则不执行用例，跳过')
    @pytest.mark.parametrize('indata,resdata', get_excel('我的商铺', 'updateshopping'))
    def test_update(self, indata, resdata, update_init):  # 列出商铺
        res =self.myshop.updata(indata, update_init[0], update_init[1])  # 商铺列出的方法
        assert res['code'] == resdata['code']
# '''
    # #手动使用环境初始化；@pytest.mark.usefixture('方法名')
    # 由于这个fixture返回的是元组，元组类型不能使用usefixtrue直接使用；
    # 可以放在函数参数中调用环境初始化方法名直接调用
    # 3-fixture update_init[0]=shopid update_init[1]=imagepath
    # '''
    # @pytest.mark.usefixtures('update_init')#由于需要使用到返回值，所以不能这样调用

if __name__ == '__main__':
    pytest.main(['test_myshop.py', '-s','-m','shop'])#-m匹配标签进行运行
    pytest.main(['test_myshop.py', '-s','-k','list'])#-k模糊匹配标签进行运行
    pytest.main(['-rs', 'test01.py'])
    '''
    用-rs执行，跳过原因才会显示SKIPPED [1] test01.py:415: 跳过Test类，会跳过类中所有方法'''