import requests

#导入请求、响应配置文件路径
from Tools.Handle_Path import REQUESTCONFIG_PATH,REPOSECONFIG_PATH

#导入配置文件数据
from Tools.Handle_Config import HandleConfigclass
VerifyDatalistURL = HandleConfigclass().read_config(REQUESTCONFIG_PATH,'Request_resource','VerifyData_list_url')
Refresh_URL = HandleConfigclass().read_config(REQUESTCONFIG_PATH,'Request_resource','refresh_token_url')
oldtoken = HandleConfigclass().read_config(REPOSECONFIG_PATH,'succeedLogin','token')
newtoken = HandleConfigclass().read_config(REPOSECONFIG_PATH,'NewsucceedLogin','newtoken')

#调用刷新接口
from Sources.Login_libs import UserClass
user = UserClass()

class DevicesListClass(object):
    def __init__(self):
        self.session = requests.Session()

    def VerifyDatalistFunction(self,url,requestdata,Authorization):
        '''
        由于刷新token接口异常，导致后续接口阻塞
        :param url:
        :param requestdata:
        :param Authorization:
        :return:
        '''
        url = VerifyDatalistURL
        headers = {"token":oldtoken,"Authorization":Authorization}
        repose = self.session.get(url=url,headers=headers,params=requestdata)

        #需要先判断是否登录凭证已失效
        if repose.json()['msg'] == '登录凭证已失效，请重新登录':
            user.RefreshFunction(url=Refresh_URL,requestData=oldtoken)
            newheaders = {"token":newtoken,"Authorization":Authorization}
            newrepose = self.session.get(url=url,headers=newheaders,params=requestdata)
            return  newrepose.json()

        elif repose.json():
            return repose.json()

if __name__ == '__main__':
    print(DevicesListClass().VerifyDatalistFunction(VerifyDatalistURL,{"page":1,"size":1},Authorization='30cc11c04808becec9792a7f0e6fedc9'))