import pytest,os,glob

from Tools.Handle_Path import TMP_DIR_PATH

#调用日志封装
from Tools.Handle_LogConfig import load_my_logging_cfg
logger = load_my_logging_cfg('Pytest_fixture')

#定义清楚Tmp临时文件的前后置函数
@pytest.fixture(scope='session')
def Clean_Tmp():
    for i in glob.glob(f'{TMP_DIR_PATH}/*.*'):
        os.remove(i)
    yield
    logger.info("清楚Tmp临时文件")