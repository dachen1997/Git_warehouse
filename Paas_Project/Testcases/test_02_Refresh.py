import pytest,allure

#导入：刷新用例文件路径、请求配置文件路径
from Tools.Handle_Path import REFRESH_TOKENYAMLDATA_PATH,REQUESTCONFIG_PATH

from Tools.Handle_yamlData import Handle_yamlDtaClass
testfile = Handle_yamlDtaClass().Handle_RefreshyamlDtaFunction(REFRESH_TOKENYAMLDATA_PATH) #获取处理后的刷新用例数据

from Tools.Handle_Config import HandleConfigclass
config = HandleConfigclass()
Refreshurl = config.read_config(REQUESTCONFIG_PATH,'Request_resource','refresh_token_url') #获取配置文件中的URL

from Tools.Handle_LogConfig import load_my_logging_cfg
logger = load_my_logging_cfg("Testing_Refresh") #调用日志器函数

from Sources.Login_libs import UserClass
User = UserClass() #调用登录源码接口

@pytest.mark.usefixtures('Clean_Tmp')
class   TestUserClass(object):

    @staticmethod
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('InputData,Result',testfile)
    @allure.feature("用户相关接口")
    @allure.story("刷新token接口")
    def testRefresh(InputData,Result):
        '''
        测试登录接口
        :param InputData:
        :param Result:
        :return:
        '''

        repose = User.RefreshFunction(url=Refreshurl,requestData=InputData)
        assert Result['code'] == repose['code'] and Result['msg'] == repose['msg']

if __name__ == '__main__':
    pass