# conftest
# 2024/4/13
#������ʼ�����������
#���������򣬷����ĸ���ֻ���ĸ��������ã������������������ǹ̶�д��conftest

import pytest
from lib.aipLib.login import Login
from lib.aipLib.myshop import myshop
'''
scope����fixture����
function Ĭ�ϣ���conftest�������µ�����def test_XX��������ǰ����ִ��
class  ��conftest�������£�ÿ��TestXXX����������ǰ����ִ��һ��
module ��conftest�������£�ÿ��test__XX ����ģ�飬����ǰ����ִ��һ�Σ�
session  ��conftest�������£������  ����ǰ��������  
'''
@pytest.fixture(scope='session', autouse=True)#auto use�Զ����ã�Ĭ��False�������ֶ�����
def start_demo(request):#����һ�����иİ��£��κ�һ��test�ļ�������һ��ʼִ�еĲ���
    print('--��ʼִ���Զ�������')

    yield #������ݲ���
    print('----�Զ������Խ���')

@pytest.fixture(scope='function')
def update_init():#�������̵Ļ�����ʼ��
    #1-��¼ �Ѿ������ʼ�������ˣ���߲���Ҫ����
    token=Login().login({'username':'admin','password':'<PASSWORD>'},gettoken=True)
    #3-�г�����ID
    shopid=myshop(token).shoplist({'page':1,'limt':10})['data']['records'][0]['id']
    #4-�ļ��ϴ�����ȡͼƬ��Ϣ
    imagepath=myshop(token).updata('123.png','../data/123.png')
    return shopid,imagepath#Ԫ�����ͣ�
    # Ԫ�����Ͳ���ʹ��usefixtrueֱ��ʹ�ã����Է��ں��������е��û�����ʼ��������ֱ�ӵ���

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