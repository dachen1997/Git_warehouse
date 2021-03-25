import pytest
import os,glob
@pytest.fixture(scope="function")
def fixturetest():#request接收params的值
    print("前置")
    yield  #获取params的值（循环获取），所以用例执行3次
    print("后置")




