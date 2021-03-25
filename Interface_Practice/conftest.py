import glob
import os
import pytest
@pytest.fixture(scope='class',autouse=False)
def Clean_tmpinfo():
    for i in glob.glob('./tmp/*.*'):
        os.remove(i)
    yield
    print("已清除tmp文件夹脏数据")