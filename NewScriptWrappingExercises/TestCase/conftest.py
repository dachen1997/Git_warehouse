import os,glob
import pytest
from Tools.Handler_Pathconfig import TmpDir_PATH

@pytest.fixture(scope='class')
def clean_tmpData():
    for i in glob.glob(f'{TmpDir_PATH}//*.*'):
        os.remove(i)
    yield
    print("清除Tmp临时json文件")

