
from pony.orm import Database
from pony.orm import (Json, PrimaryKey, Required, db_session, select, desc, Set, get, Optional)
'''
Pony规定与数据库进行交互的代码必须在数据库会话中工作
可以使用@db_session装修或db_session上下文管理数据库的工作。
当会话结束时，它会做以下操作

提交事务或则回滚事务。
返回连接池的数据库连接。
清除缓存。
'''

db = Database(provider = "mysql", host = '10.10.30.59',
                     port = 3307,
                     user = 'root',
                     password = '123456',
                     database = 'message_center',
                     charset = "utf8mb4"
              )





# conn=pymysql.connect(host = '10.10.30.59',
#                      port = 3307,
#                      user = 'root',
#                      passwd = '123456',
#                      db = 'message_center' )
# cur = conn.cursor()
# cur.execute("select * from info")






