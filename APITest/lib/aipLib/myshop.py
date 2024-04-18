# mushop
# 2024/4/12

import requests
from config.config import Host
from lib.aipLib.login import Login
class myshop:
    # ��Ҫ��������   ��Ҫ��ȡtoken
    def __init__(self, intoken):
        self.header = {'Authorization': intoken}  # ���У��
    # �г����̣���������ID
    def shoplist(self, indata):
        payload = indata
        url = f'{Host}/shopping/myshop'
        res = requests.get(url, headers=self.header, params=payload)
        return res.json()['data']['records'][0]['id']
    # �ļ��ϴ�������ͼƬ��Ϣ
    def file_upload(self, filename, filedir):
        '''
        :param filename: �ļ���
        :param filedir: �ļ�·��
        :return:
        '''
        # {'������'�����ļ������ļ�����=open(·�����򿪷�ʽ)���ļ����ͣ�}
        userfile = {'file': (filename, open(filedir, 'rb'), 'image/png')}
        res = requests.post(f'{Host}/file', files=userfile, headers=self.header)
        return res.json()['data']['realFileName']  # ����ͼƬ��Ϣ

    # �༭����
    # ��Ҫ����id shopid ���г������л�ȡ
    # ͼƬ��Ϣ  imagepath   ���ϴ��ӿڷ���
    def updata(self, indata, shopid, imagepath):
        # indata����excel����������������
        # ����ID
        indata['id'] = shopid
        # ����ͼƬ��Ϣ
        indata['image_path'] = imagepath
        # ����image��Ϣ
        indata['image'] = f'{Host}/file/getImgStream?fimeName={imagepath}'
        payload = indata
        url = f'{Host}/shopping/updatemyshop'
        res = requests.post(url, headers=self.header, data=payload)
        return res.json()


if __name__ == '__main__':
    # 1-��¼�ɹ�������tokenֵ
    token = Login().login({"username": "admin", "password": "<PASSWORD>"}, gettoken=True)
    # 2-�г��ҵ����̣���������id
    shopid = myshop(token).shoplist({'page': 1, 'limit': 10})
    # 3-�ļ��ϴ�������ͼƬ��Ϣ
    imagepath = myshop(token).file_upload('123.png', '../../data/123.png')
    # 4-�༭����
    info={


    }
    myshop(token).update(info, shopid, imagepath)

