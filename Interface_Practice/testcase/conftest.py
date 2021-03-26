# import pytest
# import os,glob
# @pytest.fixture(scope="function")
# def fixturetest():#request接收params的值
#     print("前置")
#     yield  #获取params的值（循环获取），所以用例执行3次
#     print("后置")
import os,glob
import pytest
@pytest.fixture(scope='class')
def Clean_tmpinfo():
    for i in glob.glob('../tmp/*.*'):
        os.remove(i)
    yield
    print("已清除tmp文件夹脏数据")



