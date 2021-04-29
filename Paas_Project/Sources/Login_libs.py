import requests

from Tools.Handle_Path import REQUESTCONFIG_PATH,REPOSECONFIG_PATH #导入请求和响应配置文件

#处理配置文件信息，获取登录和刷新接口的URL
from Tools.Handle_Config import HandleConfigclass
config = HandleConfigclass()
login_url = config.read_config(REQUESTCONFIG_PATH,'Request_resource','login_url')
refresh_url = config.read_config(REQUESTCONFIG_PATH,'Request_resource','refresh_token_url')

#这个是做调试用的token数据
refresh_token = config.read_config(REPOSECONFIG_PATH,'succeedLogin','token')

#调用日志封装
from Tools.Handle_LogConfig import load_my_logging_cfg
logger = load_my_logging_cfg('Sources_Login_libs')

class   UserClass(object):
    '''
    用Session会话发送请求，会自动管理cookie，作为属性
    '''
    def __init__(self):
        self.session = requests.Session()

    def LoginFunction(self,url,requestData,is_token=False):
        try:
            url = login_url
            repose = self.session.post(url=url,json=requestData)

            #成功登录时，写入token到配置文件
            if repose.json()['code'] == 0 and repose.json()['msg'] == "登录成功！" and repose.json():
                data = {'succeedLogin': {"TOKEN": repose.json()['data']}}
                config.write_config(datas=data, filename=f'{REPOSECONFIG_PATH}')

            if  is_token == True:
                return repose.json()['data']
            else:
                return repose.json()

        except Exception:
            logger.warning("请求异常")

    def RefreshFunction(self,url,requestData,is_token=False):
        '''
        刷新接口有bug，无法成功刷新token，刷新后始终为老的token
        :param url:
        :param requestData:
        :param is_token:
        :return:
        '''
        URL = refresh_url
        repose = self.session.post(url=URL,json=requestData)

        #接口成功刷新时，写入新的token到配置文件
        if repose.json()['code'] == 0 and repose.json()['msg'] == "成功" and repose.json():
            data = {'NewsucceedLogin': {"NEWTOKEN": repose.json()['data']}}
            config.write_config(datas=data, filename=f'{REPOSECONFIG_PATH}')

        if  is_token == True:
            return repose.json()['data']
        else:
            return repose.json()

if __name__ == '__main__':
    obj = UserClass()
    res = obj.LoginFunction(login_url,{"username":"847w","password":"1A52"})
    res1 = obj.RefreshFunction(refresh_url,{"token":refresh_token})
    print(res)
    print(res1)