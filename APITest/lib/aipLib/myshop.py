# mushop
# 2024/4/12

import requests
from config.config import Host
from lib.aipLib.login import Login
class myshop:
    # 需要操作商铺   需要获取token
    def __init__(self, intoken):
        self.header = {'Authorization': intoken}  # 身份校验
    # 列出商铺，返回商铺ID
    def shoplist(self, indata):
        payload = indata
        url = f'{Host}/shopping/myshop'
        res = requests.get(url, headers=self.header, params=payload)
        return res.json()['data']['records'][0]['id']
    # 文件上传，返回图片信息
    def file_upload(self, filename, filedir):
        '''
        :param filename: 文件名
        :param filedir: 文件路径
        :return:
        '''
        # {'变量名'，（文件名，文件对象=open(路径，打开方式)，文件类型）}
        userfile = {'file': (filename, open(filedir, 'rb'), 'image/png')}
        res = requests.post(f'{Host}/file', files=userfile, headers=self.header)
        return res.json()['data']['realFileName']  # 返回图片信息

    # 编辑商铺
    # 需要商铺id shopid 从列出方法中获取
    # 图片信息  imagepath   从上传接口返回
    def updata(self, indata, shopid, imagepath):
        # indata来自excel用例里面的请求参数
        # 更新ID
        indata['id'] = shopid
        # 更新图片信息
        indata['image_path'] = imagepath
        # 更新image信息
        indata['image'] = f'{Host}/file/getImgStream?fimeName={imagepath}'
        payload = indata
        url = f'{Host}/shopping/updatemyshop'
        res = requests.post(url, headers=self.header, data=payload)
        return res.json()


if __name__ == '__main__':
    # 1-登录成功，返回token值
    token = Login().login({"username": "admin", "password": "<PASSWORD>"}, gettoken=True)
    # 2-列出我的商铺，返回商铺id
    shopid = myshop(token).shoplist({'page': 1, 'limit': 10})
    # 3-文件上传，返回图片信息
    imagepath = myshop(token).file_upload('123.png', '../../data/123.png')
    # 4-编辑商铺
    info={


    }
    myshop(token).update(info, shopid, imagepath)

