import os,glob
import pytest

from Tools.Handler_Pathconfig import TmpDir_PATH

from Tools.Handler_Mysql import Handle_mysql

from Tools.Handler_Logconfig import load_my_logging_cfg
logger = load_my_logging_cfg("fixture_CaoZuo")

@pytest.fixture(scope='class')
def clean_tmpData():
    for i in glob.glob(f'{TmpDir_PATH}//*.*'):
        os.remove(i)
    yield
    logger.info("清除Tmp临时json文件")
