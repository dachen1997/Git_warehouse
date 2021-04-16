import random

import pymysql
from Config.configData import *
from Tools.Handler_Logconfig import *
logger = load_my_logging_cfg("Mysql")

class Handle_mysql:
    def __init__(self):
        self.db = pymysql.connect(host=f"{sqlhost}",
                                  port=sqlport,
                                  user=f"{sqluser}",
                                  passwd=f"{sqlpasswd}",
                                  database=f"{sqldatabase}",
                                  charset="utf8",
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
        self.cursor = self.db.cursor()

    def GettingSqlData(self,sql,is_fetchall=True):
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
        self.cursor.close()
        self.db.close()

    def Create_tel(self):
        one_tel = random.choice(['152', '187', '158', '136','137'])
        two_tel = random.sample('12345678', 8)
        fintel = one_tel + "".join(two_tel)  # 生成随机手机号
        return fintel

    def is_exited_tel(self,tel):
        db = Handle_mysql()
        res = db.GettingSqlData(f"select * from OWNERINFO where OWNERINFO.STR_TEL='{tel}'")
        while 1:
            if  res:
                continue
            else:
                return tel
                break
        db.CloseSql()
if __name__ == '__main__':
    mysql = Handle_mysql()
    create_tel = mysql.Create_tel()
    res_tel = mysql.is_exited_tel(create_tel)
    mysql.CloseSql()
    print(res_tel)