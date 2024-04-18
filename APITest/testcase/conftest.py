# conftest
# 2024/4/13
# ������ʼ�����������
# ���������򣬷����ĸ���ֻ���ĸ��������ã������������������ǹ̶�д��conftest

import pytest
from lib.aipLib.login import Login
from lib.aipLib.myshop import myshop
from config.config import username

'''
scope����fixture����
function Ĭ�ϣ���conftest�������µ�����def test_XX��������ǰ����ִ��
class  ��conftest�������£�ÿ��TestXXX����������ǰ����ִ��һ��
module ��conftest�������£�ÿ��test__XX ����ģ�飬����ǰ����ִ��һ�Σ�
session  ��conftest�������£������  ����ǰ��������  
'''


@pytest.fixture(scope='session', autouse=True)  # auto use�Զ����ã�Ĭ��False�������ֶ�����
def start_demo(request):  # ����һ�����иİ��£��κ�һ��test�ļ�������һ��ʼִ�еĲ���
    print('--��ʼִ���Զ�������')

    yield  # ������ݲ���
    print('----�Զ������Խ���')


'''
fixture�÷�
1��ʹ�ú�����ֱ�ӵ��ã�����û�з���ֵ
@pytest.mark.usefixtures('update_init')#д�뺯����
2����Ҫʹ��fixture�ķ���ֵʱ
ֱ���ٶ�Ӧ�Ľӿں����У�����һ���βΣ�����������fixture������

'''

'''
����㣺
1�����̸��½ӿڣ�ÿ�β�������ҪҪ��¼��----����
2����¼����-����ģ��Ҳ��Ҫ
3�����ҵ��Ƚϸ��ӣ���Ҫǰ����������ģ�黯
'''
'''
���������
1������¼���������������
2�����̵�ʵ����������������
3������һ��ģ��Ĳ��ԣ�ֻ��Ҫ��¼һ��
'''


# 1-����¼�������
@pytest.fixture(scope='class')
def Login_init():
    token = Login().login(username, gettoken=True)
    return token


# 2-����ʵ���� -������Ҫ����token��fixture
@pytest.fixture(scope='class')
def myshop_init(Login_init):
    # ����һ��fixture����Ҫfixture�ķ���ֵ�����Խ���һ��fixture�����β�ȥ����
    shop = myshop(Login_init)
    return shop


# 3-���̸���ǰ��ǰ�ò���
@pytest.fixture(scope='function')
def update_init(myshop_init):  # �������̵Ļ�����ʼ��
    shopid = myshop_init.shoplist({'page': 1, 'limt': 10})['data']['records'][0]['id']
    # 4-�ļ��ϴ�����ȡͼƬ��Ϣ
    imagepath = myshop_init.updata('123.png', '../data/123.png')
    return shopid, imagepath  # Ԫ�����ͣ�
    # Ԫ�����Ͳ���ʹ��usefixtrueֱ��ʹ�ã����Է��ں��������е��û�����ʼ��������ֱ�ӵ���
