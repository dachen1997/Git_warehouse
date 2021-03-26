import yaml

from libs.login_libs import Login#导入登录方法
from tools.logindata import getting_logindata#导入登录的测试数据
data = getting_logindata(r'../data/test_login_data.yaml',False)#获取登录数据，格式为yaml原始数据格式

tokenlist = [] #用于存放正确的token

for i in range(len(data)):
    oldtoken = Login().login(data[i]['data'], False)  # 调取登录方法,获取oldtoken
    if oldtoken is not None:
        tokenlist.append(oldtoken)#获取正确oldtoken存入列表中
    else:
        continue #为空时不存入

def flash_token_data(file):#定义获取token函数
    file = open(file, 'r', encoding='utf-8')#打开yaml文件
    res = yaml.load(file,Loader=yaml.FullLoader)
    res[0]['data']['token']=tokenlist[0]#将flash_token_data.yaml文件第一个用例的oldtoken写入
    datalist = [] #用于用例数据驱动存放特定格式的用例数据列表
    for i in range(len(res)):
        datalist.append((res[i]['data'],res[i]['result']))
    return datalist

if __name__ == '__main__':
    print(flash_token_data(r'../data/flash_token_data.yaml'))