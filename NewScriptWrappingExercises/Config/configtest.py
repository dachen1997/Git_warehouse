import configparser
from Tools.Handler_Pathconfig import ConfigDir_PATH
#创建配置解析模块configparser的方法ConfigParser（）的对象  config
config = configparser.ConfigParser()

#写入就是像写入字典那样
#用法1    直接把section的键值对写入到字典
config["DEFAULT"]={"name":"dachen","age":"24"}

#用法2    逐级的添加键值对
config["section1"] = {}
config["section1"]["key"] = "value"

#用法3    把初始化的section先赋值给一个变量，然后添加其他键值对
config["section2"] = {}
section3 = config["section2"]
section3["testkey"] = "testvalues"

# with open(r'config.ini','w',encoding='utf-8') as test:
#     config.write(test)

#读取配置文件内容
config.read(f'{ConfigDir_PATH}/config.ini')#要先读取配置文件
res = config.sections()#获取所有section

print(res)
print(config['section1']['key'])#读取文件后就可以通过section的键获取值

from  Tools.Handle_Config import HandleConfigclass
newconfig = HandleConfigclass()
URL = newconfig.read_config(r'config.ini','InterfaceData','URL')
sqlhost = newconfig.read_config(r'config.ini','mysqlData','sqlhost')
sqlport = newconfig.read_config(r'config.ini','mysqlData','sqlport')
sqluser = newconfig.read_config(r'config.ini','mysqlData','sqluser')
sqlpasswd = newconfig.read_config(r'config.ini','mysqlData','sqlpasswd')
sqldatabase = newconfig.read_config(r'config.ini','mysqlData','sqldatabase')
pass