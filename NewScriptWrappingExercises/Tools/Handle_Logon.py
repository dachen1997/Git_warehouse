import random
import yaml
from Tools.Handler_Mysql import Handle_mysql
from Tools.Handler_Pathconfig import DataDir_PATH
from Tools.Handler_Logconfig import load_my_logging_cfg
logger = load_my_logging_cfg("logon")

def Handlelogondata(file,is_list=True):
    data = open(file,'r',encoding='utf-8')
    fin = yaml.load(data,Loader=yaml.FullLoader)#读取yaml文件内容
    finlist = []
    for i in range(len(fin)):
        finlist.append((fin[i]['data'],fin[i]['result']))#生成列表嵌套的测试数据，用作pytest的数据驱动

    while 1:
        one_tel = random.choice(['152', '187', '158', '136'])
        two_tel = random.sample('12345678', 8)
        fintel = one_tel + "".join(two_tel)#生成随机手机号

        res = Handle_mysql().GettingSqlData(f"select * from OWNERINFO where OWNERINFO.STR_TEL='{fintel}' ")

        if res:#为真代表有数据，不插入
            logger.info("该账号已注册")
            continue
        else:#为假，代表数据库没此手机号，可以插入，作为测试数据
            logger.info("该账号未注册")
            finlist[0][0]['telphone']=fintel#插入未注册的手机号
            break
    Handle_mysql().CloseSql()#关闭数据库
    if is_list==True:
        return finlist
    else:
        return fin



if __name__ == '__main__':
    fininfo = Handlelogondata(f'{DataDir_PATH}//logonDataTest.yaml')
    print(fininfo)