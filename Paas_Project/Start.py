import os,pytest
from Tools.Handle_Path import TMP_DIR_PATH,REPORT_DIR_PATH

if __name__ == '__main__':
    pytest.main()
    os.system(f'allure generate {TMP_DIR_PATH} -o {REPORT_DIR_PATH} --clean ')