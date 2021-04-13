
import pytest
import os
from Tools.Handler_Pathconfig import TmpDir_PATH,Report_PATH

if __name__ == '__main__':
    pytest.main()
    os.system(f'allure generate {TmpDir_PATH} -o {Report_PATH} --clean')