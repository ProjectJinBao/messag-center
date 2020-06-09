def name():
    # -*- coding:utf-8 -*-
    import uuid
    uuid_num = uuid.uuid1()


    onlyname = "你好" + str(uuid_num)
    return onlyname



class Msql_query(object):

    def __init__(self):
        import pymysql

        self.db = pymysql.connect(
            host='10.10.30.59',
            port=3307,
            user="root",
            password="123456",
            db="message_center")

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def get_contetn_name(self):
        sql_query = "select name from content where isdelete is not True"
        self.cursor.execute(sql_query)
        # 使用 fetchone() 方法获取一条数据,类型为元组
        data = self.cursor.fetchone()
        # 关闭数据库连接
        self.db.close()
        return data[0]
Msql_query().get_contetn_name()

# sql_query_robots = "selete key from info"
# self.cursor.execute(sql_query)
# key_r = self.cursor.fetchone()