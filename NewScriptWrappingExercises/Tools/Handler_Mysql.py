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
        logger.info("cursor游标关闭")
        self.db.close()
        logger.info("数据库对象关闭")

if __name__ == '__main__':
    res = Handle_mysql().GettingSqlData("select * from OWNERINFO where OWNERINFO.STR_TEL='14700000000'")
    if res:
        print("===")
    else:
        print("sssss")
    Handle_mysql().CloseSql()
    print(res)