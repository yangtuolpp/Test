# login
# 2024/4/12
import requests
import hashlib
import json
from config.config import Host#导入配置
import copy
class Login(object):
    def get_mad5(self,pws):
        md5 = hashlib.md5()#实例化
        md5.update(pws.encode('utf-8'))#进行加密
        return md5.hexdigest()  # 获取加密结果
    def login(self,indata,gettoken=True):#实例方法
        url=f"{Host}auth/login"

        payload = copy.copy(indata)#规避使用用户名密码全局变量后，密码重复加密的报错
        payload['password']= self.get_mad5(payload['password'])#参数

        res=requests.post(url,data=payload)
        if gettoken:
            return res.json()['data']['token']
        else:
            return res.json()
if __name__ == '__main__':

    print(Login().login('''{"username":"admin","password":"1111"}'''))