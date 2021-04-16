import requests
from Config.configData import URL
from Tools.Handler_Logconfig import load_my_logging_cfg
logger = load_my_logging_cfg("testname")
class   Login_Flash():
    def __init__(self):
        self.session = requests.Session()

    def login(self,url,method,data,is_json=True,**args):
        try:
            if method.lower()=="post":
                res = self.session.post(url,json=data)
                return res.json()
            elif method.lower()=="post" and is_json==False:
                res = self.session.post(url, data=data)
                return res.json()
            else:
                logger.debug("只有post请求方式")
        except Exception:
            logger.warning("请输入正确参数内容")

if __name__ == '__main__':
    finInfo = Login_Flash().login(url=f"{URL}/thirdPartyLogin",method="post",data={"username":"847w","password":"1A52"})
    print(finInfo)