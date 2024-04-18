# test_myshop
# 2024/4/12
import pytest
from lib.aipLib.login import Login
from lib.aipLib.myshop import myshop
from tools.getdata import get_excel
from config.config import username
@pytest.mark.shop#�������ӱ�ǩ������ѡ���Ե�ĳһ���ǩ������
class TestMyShop():
    def setup_class(self):
        #����ʵ����ֻ���¼һ�Σ�����ʹ�ò�����---�����ļ�ʵ��;
        #��config�н��û����������������username�������ã��������ĵĻ�����
        self.token = Login().login(username, gettoken=True)
        #ÿ�ζ�Ҫ��������ʵ�������Կ�����ǰ�ó�ʼ���д���ʵ��������ʹ��ʱ���ü���
        self.myshop = myshop(self.token)
    #�г�����

    @pytest.mark.shop_list#�������ӱ�ǩ������ѡ���Ե�ĳһ���ǩ������
    @pytest.mark.parametrize('indata,resdata', get_excel('�ҵ�����', 'listshopping'))
    def test_myshoplist(self, indata, resdata):
        res = self.myshop.shoplist(indata)
        if 'code' in res:
            assert res['code'] == resdata['code']
        else:
            assert res['error'] == resdata['error']

    #2-���µ���
    #��ִ�е��̸��µĽӿ�ʱ������Ҫ��¼����������һЩǰ�ò��������ϴ��ļ�
    #ֻ�и��µ��̵Ľӿ���Ҫ�������ӿڲ���Ҫ���ǾͲ��ܷ���setup��
    #fixture������ʼ�����������������������������setup��teardown��һ��
    #fixture������ĳ���ض������������У�ֻ��Ҫ���ü��ɣ���setup��teardown����
    @pytest.mark.update#�������ӱ�ǩ������ѡ���Ե�ĳһ���ǩ������
    #����������
    @pytest.mark.skip(reason='��ִ������')#����������
    #��������
    @pytest.mark.skipif(1==2,reason='����������㣬��ִ������������')
    @pytest.mark.parametrize('indata,resdata', get_excel('�ҵ�����', 'updateshopping'))
    def test_update(self, indata, resdata, update_init):  # �г�����
        res =self.myshop.updata(indata, update_init[0], update_init[1])  # �����г��ķ���
        assert res['code'] == resdata['code']
# '''
    # #�ֶ�ʹ�û�����ʼ����@pytest.mark.usefixture('������')
    # �������fixture���ص���Ԫ�飬Ԫ�����Ͳ���ʹ��usefixtrueֱ��ʹ�ã�
    # ���Է��ں��������е��û�����ʼ��������ֱ�ӵ���
    # 3-fixture update_init[0]=shopid update_init[1]=imagepath
    # '''
    # @pytest.mark.usefixtures('update_init')#������Ҫʹ�õ�����ֵ�����Բ�����������

if __name__ == '__main__':
    pytest.main(['test_myshop.py', '-s','-m','shop'])#-mƥ���ǩ��������
    pytest.main(['test_myshop.py', '-s','-k','list'])#-kģ��ƥ���ǩ��������
    pytest.main(['-rs', 'test01.py'])
    '''
    ��-rsִ�У�����ԭ��Ż���ʾSKIPPED [1] test01.py:415: ����Test�࣬�������������з���'''