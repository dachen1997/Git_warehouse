import pytest,allure

#导入登录接口用例文件路径、请求配置文件路径
from Tools.Handle_Path import LOGIN_YAMLDATA,REQUESTCONFIG_PATH

# 获取处理后的登录用例数据
from Tools.Handle_yamlData import Handle_yamlDtaClass
testfile = Handle_yamlDtaClass().Handle_yamlDtaFunction(LOGIN_YAMLDATA)

#获取配置文件中的URL
from Tools.Handle_Config import HandleConfigclass
loginurl = HandleConfigclass().read_config(REQUESTCONFIG_PATH,'Request_resource','login_url')

#调用日志器函数
from Tools.Handle_LogConfig import load_my_logging_cfg
logger = load_my_logging_cfg("Testing_login")

#调用登录源码接口
from Sources.Login_libs import UserClass
User = UserClass()

#导入MySQL封装
from Tools.Handle_Mysql import Handlemysqlclass
db = Handlemysqlclass()

@pytest.mark.usefixtures('Clean_Tmp')
class   TestUserClass(object):

    @staticmethod
    def setup_class():
        logger.info("已连接数据库")

    @staticmethod
    def teardown_class():
        db.CloseSql()
        logger.info("关闭数据库")

    @staticmethod
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('InputData,Result,Testtitle',testfile)
    @allure.feature("用户相关接口")
    @allure.story("登录接口")
    def testLogin(InputData,Result,Testtitle):
        '''
        测试登录接口
        :param InputData:
        :param Result:
        :return:
        '''
        logger.info(Testtitle)
        repose = User.LoginFunction(url=loginurl,requestData=InputData)
        assert Result['code'] == repose['code'] and Result['msg'] == repose['msg']

if __name__ == '__main__':
    pass