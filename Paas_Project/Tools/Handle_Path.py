import os
#项目根目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件相关路径
CONFIGS_DIR_PATH = os.path.join(BASE_PATH,'Configs')
MYSQLCONFIG_PATH = os.path.join(CONFIGS_DIR_PATH,'MysqlConfig.ini')
REQUESTCONFIG_PATH = os.path.join(CONFIGS_DIR_PATH,'RequestConfig.ini')
REPOSECONFIG_PATH = os.path.join(CONFIGS_DIR_PATH,'ReposeConfig.ini')

#yaml相关路径
DATAS_DIR_PATH = os.path.join(BASE_PATH,'Datas')
LOGIN_YAMLDATA = os.path.join(DATAS_DIR_PATH,'Login_yamlData.yaml')
REFRESH_TOKENYAMLDATA_PATH = os.path.join(DATAS_DIR_PATH,'Refresh_tokenyamlData.yaml')
VERIFYDATALIST_YAMLDATA_PATH = os.path.join(DATAS_DIR_PATH,'VerifyDatalist_yamlData.yaml')

#report相关路径
REPORT_DIR_PATH = os.path.join(BASE_PATH,'Report')

#Tmp相关路径
TMP_DIR_PATH = os.path.join(BASE_PATH,'Tmp')

#Log相关路径
LOG_DIR_PATH = os.path.join(BASE_PATH,'Log')

if __name__ == '__main__':
    pass