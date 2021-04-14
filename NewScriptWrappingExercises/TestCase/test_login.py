import pytest
import allure
from Config.configData import URL
from Source.User_Related_Interface import Login_Flash
from Tools.Handler_LoginData import getting_logindata
from Tools.Handler_Pathconfig import DataDir_PATH

res = getting_logindata(f'{DataDir_PATH}//loginData.yaml',is_list=True)

@pytest.mark.usefixtures('clean_tmpData')
class   Test_about_login():

    @allure.feature('登录')
    @pytest.mark.parametrize("indata,finresult",res)
    def testlogin(self,indata,finresult):
        finInfo = Login_Flash().login(url=f"{URL}/thirdPartyLogin",method="post",data=indata)
        assert finresult['code']==finInfo['code'] and finresult['msg']==finInfo['msg']