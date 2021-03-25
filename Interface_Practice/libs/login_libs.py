import requests
import hashlib
import json
from config.global_info import HOST

def get_passwd_md5(passwd):
    MD5 = hashlib.md5()
    MD5.update(passwd.encode('utf-8'))
    return MD5.hexdigest()

class   Login():
    def login(self,inputRequestDate,choice):
        url = f'{HOST}/api/loginS'
        headers = {"Content-Type":"application/json"}
        inputRequestDate['password']=get_passwd_md5(inputRequestDate['password'])
        body = inputRequestDate
        req = requests.post(url,data=json.dumps(body),headers=headers)
        if choice==True:
            return req.json()['token']
        else:
            return req.json()

if __name__ == '__main__':
    print(Login().login({"username":"20154084","password":"123456"},True))