# -*- coding: utf-8 -*-

from  database.mysql_conn import db
import datetime
from pony.orm import (Json, PrimaryKey, Required, db_session, select, desc, Set, get, Optional)
from utils.exception_handle import IsExist, IsNotExist

class Info(db.Entity):
    _table_ = 'info'
    id = PrimaryKey(int, auto = True) #autoBoolean 是否自增
    key = Required(str, 50)
    name = Required(str, 30, default = "未知") #如果是必须的话必须加默认值
    url = Optional(str, 100)
    comment = Optional(str, 50, nullable = True)
    create_time = Required(datetime.datetime, default = datetime.datetime.now(), nullable = True)
    update_time = Required(datetime.datetime, default = datetime.datetime.now(), nullable = True)

    @classmethod #类方法的装饰器。表明此方法可以直接被类对象调用
    @db_session #数据库会话的装饰器，被此装饰器装饰的方法，内部的代码都运行在是数据库会话的上下文之间
    #获取企业微信机器人的信息
    def db_get_info(self):
        objs = select(n for n in Info)
        data = []
        for obj in objs:
            dict = {"id": obj.id,
                    "name": obj.name,
                    "url": obj.url,
                    "comment": obj.comment,
                    "create_time": obj.create_time,
                    "key": obj.key,
                    "update_time": obj.update_time
                    }
            data.append(dict)
        return data

    #上传企业微信机器人信息
    @classmethod
    @db_session
    def db_creat_info(cls, url, name, comment, key):
        obj = get(n for n in Info if n.url == url)
        if obj:
            raise IsExist(title='该url已经存在', detail=f'url为{url}的机器人已经存在')
        #需要添加正在匹配，将key单独存储
        else:
            Info(url = url, name = name, comment = comment, key = key)

    @classmethod
    @db_session
    def db_update_info(self, url, name, comment, key):
        obj = get(n for n in Info if n.key == key)
        if obj:
            obj.name = name
            obj.url = url
            obj.comment = comment
            obj.update_time = datetime.datetime.now()
        else:
            raise IsNotExist(title = '修改机器人不存在', detail = f'key={key}的机器人不存在')

    @classmethod
    @db_session
    def db_del_info(self,key):
        obj = get(n for n in Info if n.key == key)
        print(key)
        if obj:
           obj.delete()
        else:
            raise IsNotExist(title='删除机器人不存在', detail=f'key={key}的机器人不存在')
