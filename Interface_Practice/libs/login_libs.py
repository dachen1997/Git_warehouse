# #MD5加密
# import hashlib
# def get_passwd_md5(passwd):
#     MD5 = hashlib.md5()
#     MD5.update(passwd.encode('utf-8'))
#     return MD5.hexdigest()


import requests
import json
from config.global_info import HOST

class Login():
    def login(self,indata,choice): #登录方法源码
        url = f'{HOST}/thirdPartyLogin'
        res = requests.post(url,data=json.dumps(indata))
        if choice==True:
            return res.json()
        else:
            return res.json()['data']

    def flash_token(self,old_token,choice): #刷新token方法源码
        url = f'{HOST}/refresh'
        res = requests.post(url,json=old_token)
        if choice==True:
            return res.json()
        else:
            return res.json()['data']

if __name__ == '__main__':
    print(Login().login({'username': '847w', 'password': '1A52'},True))
    token = Login().login({'username': '847w', 'password': '1A52'},False)
    print(Login().flash_token({"token":token},True))



