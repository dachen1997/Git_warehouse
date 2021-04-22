import pytest
import allure
from Config.configData import URL

from Source.User_Related_Interface import Login_Flash

from Tools.Handler_LoginData import getting_logindata

from Tools.Handler_Pathconfig import DataDir_PATH
res = getting_logindata(f'{DataDir_PATH}//loginData.yaml',is_list=True)

from Tools.Handler_Mysql import Handle_mysql

from Tools.Handler_Logconfig import load_my_logging_cfg
logger = load_my_logging_cfg("mysql")

@pytest.mark.usefixtures('clean_tmpData')
class   Test_about_login():

    def setup_class(self):
        Handle_mysql()
        logger.info("连接MySQL")

    def teardown_class(self):
        Handle_mysql().CloseSql()
        logger.info("关闭Mysql")

    @allure.feature('登录')
    @pytest.mark.parametrize("indata,finresult",res)
    @pytest.mark.run(order=1)
    def testlogin(self,indata,finresult):
        '''
        数据校验可以在yaml文件中增加个标识字段，然后拿出来进行判断
        :param indata:
        :param finresult:
        :return:
        '''
        if  finresult['is_sendSQL']=='yes':
            db = Handle_mysql()
            sql = "select OWNERINFO.STR_NICKNAME from OWNERINFO where OWNERINFO.STR_TEL='18351816010'"
            db.GettingSqlData(sql)
            finInfo = Login_Flash().login(url=f"{URL}/thirdPartyLogin",method="post",data=indata)
            assert finresult['code']==finInfo['code'] and\
                   finresult['msg']==finInfo['msg']
