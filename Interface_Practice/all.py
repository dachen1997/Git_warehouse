import os
import pytest
if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./tmp -o ./report --clean')