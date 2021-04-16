import yaml
from Tools.Handler_Mysql import Handle_mysql

from Tools.Handler_Pathconfig import DataDir_PATH

from Tools.Handler_Logconfig import load_my_logging_cfg

logger = load_my_logging_cfg("logon")

def Handlelogondata(file,is_list=True):
    data = open(file,'r',encoding='utf-8')
    fin = yaml.load(data,Loader=yaml.FullLoader)#读取yaml文件内容
    logger.info("读取注册yaml文件测试数据")
    finlist = []
    for i in range(len(fin)):
        finlist.append((fin[i]['data'],fin[i]['result']))#生成列表嵌套的测试数据，用作pytest的数据驱动
    if is_list:
        db = Handle_mysql()
        newtel = db.Create_tel()
        fintel = db.is_exited_tel(newtel)
        finlist[0][0]['telphone'] = fintel#low版的动态数据替换
        Handle_mysql().CloseSql()
        logger.info("返回数据驱动式的注册数据列表形式")
        return finlist
    else:
        return fin

if __name__ == '__main__':
    fininfo = Handlelogondata(f'{DataDir_PATH}//logonDataTest.yaml')
    print(fininfo)