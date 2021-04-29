import random

import pymysql

from Tools.Handle_Path import MYSQLCONFIG_PATH #导入配置文件路径

from Tools.Handle_Config import HandleConfigclass #导入配置文件数据
config = HandleConfigclass()
sqlhost = config.read_config(MYSQLCONFIG_PATH,'sql_connect_info','host')
sqlport = config.read_config(MYSQLCONFIG_PATH,'sql_connect_info','port')
sqluser = config.read_config(MYSQLCONFIG_PATH,'sql_connect_info','user')
sqlpasswd = config.read_config(MYSQLCONFIG_PATH,'sql_connect_info','passwd')
sqldatabases = config.read_config(MYSQLCONFIG_PATH,'sql_connect_info','databases')

#导入日志封装
from Tools.Handle_LogConfig import load_my_logging_cfg
logger = load_my_logging_cfg("Mysql")

class Handlemysqlclass:
    def __init__(self):
        self.db = pymysql.connect(host=f"{sqlhost}",
                                  port=int(sqlport),
                                  user=f"{sqluser}",
                                  passwd=f"{sqlpasswd}",
                                  database=f"{sqldatabases}",
                                  charset="utf8",
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
        self.cursor = self.db.cursor()

    def GettingSqlData(self,sql,is_fetchall=True):
        '''
        获取SQL语句的执行结果，is_fetchall=True 获取多行输出    is_fetchall=False 获取当行输出
        :param sql:
        :param is_fetchall:
        :return:
        '''
        try:
            self.cursor.execute(sql)
            self.db.commit()
            if is_fetchall==False:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchall()
        except Exception:
            self.db.rollback()
            logger.warning("错误操作")

    def CloseSql(self):
        '''
        关闭操作游标和数据库连接对象
        :return:
        '''
        self.cursor.close()
        self.db.close()

    def Create_tel(self):
        '''
        生成手机号方法
        :return:
        '''
        one_tel = random.choice(['152', '187', '158', '136','137'])
        two_tel = random.sample('12345678', 8)
        fintel = one_tel + "".join(two_tel)  # 生成随机手机号
        return fintel

    def is_exited_tel(self,tel,decide_sql):
        '''
        通过带有手机号字段的SQL语句判断手机号是否存在，存在时继续循环判断，返回的是不存在的手机号
        :param tel:
        :param sql:
        :return:
        '''
        db = Handlemysqlclass()
        res = db.GettingSqlData(decide_sql)
        while 1:
            if  res:
                continue
            else:
                return tel
                break
        db.CloseSql()

if __name__ == '__main__':
    pass