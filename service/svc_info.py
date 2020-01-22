
from database.mysql_conn import db
from database.db_info import Info
from utils.match import re_search

#获取企业微信机器人信息
def svc_get_info():
    # db.generate_mapping(create_tables=True)
    data = Info.db_get_info()
    return data

#上传企业微信机器人信息到数据库中
def svc_creat_info(body):
    name = body.get("name")
    url = body.get("url")
    comment = body.get("comment")
    key = re_search(url)
    Info.db_creat_info(url=url, name=name, comment=comment, key=key)

def svc_put_info(key, body):
    name = body.get("name")
    url = body.get("url")
    comment = body.get("comment")
    Info.db_update_info(url=url, name=name, comment=comment,key=key)

def svc_del_info(key):
    print(key)
    Info.db_del_info(key)