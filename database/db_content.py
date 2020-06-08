
from  database.mysql_conn import db
import datetime
from pony.orm import (Json, PrimaryKey, Required, db_session, select, desc, Set, get, Optional)
from utils.exception_handle import IsExist, IsNotExist

class Content(db.Entity):
    _table_ = 'content'
    id = PrimaryKey(int, auto=True)
    msgtype = Required(str, 30, default="text")
    name = Required(str, 50, unique=True)
    content = Required(str)
    isdelete = Optional(bool)
    create_time = Required(datetime.datetime, default=datetime.datetime.now(), nullable=True)
    update_time = Required(datetime.datetime, default=datetime.datetime.now(), nullable=True)
    # project = Optional(str)
    # sprint = Optional(str)

    @classmethod
    @db_session
    def db_create_content(cls, msgtype, name, content):
        obj = get(n for n in Content if n.name == name)
        if obj:
            raise IsExist(title='该名字的模版已经存在', detail=f'name为【{name}】的模版已经存在')
        else:
            Content(msgtype=msgtype, name=name, content=str(content), create_time=datetime.datetime.now(), isdelete=0)

    @classmethod
    @db_session
    def db_get_content(cls):
        objs = select(n for n in Content if n.isdelete==0)
        data = []
        for obj in objs:
            dict = {
                "name": obj.name,
                "content": obj.content,
                "msgtype": obj.msgtype,
                # "project": obj.project,
                # "sprint": obj.sprint
            }
            data.append(dict)
        return data

    @classmethod
    @db_session
    def db_update_content(cls, msgtype, name, content, project, sprint):
        obj = get(n for n in Content if n.name == name and n.isdelete == 0)
        if obj:
            obj.msgtype = msgtype
            obj.content = content
            # obj.project = project
            # obj.sprint = sprint
            obj.update_time = datetime.datetime.now()
        else:
            raise IsNotExist(title='没有该名字的模版', detail=f'没有名为【{name}】的模版')

    @classmethod
    @db_session
    def db_delete_content(cls, name):
        obj = get(n for n in Content if n.name==name and n.isdelete == 0)
        if obj:
            obj.isdelete = 1
            obj.update_time = datetime.datetime.now()
        else:
            raise IsNotExist(title='没有该名字的模版',detail=f'没有名字为【{name}】的模版')

    @classmethod
    @db_session
    def db_content(cls, name):
        obj = get(n for n in Content if n.name==name and n.isdelete == 0)
        if obj:
            return {
                "content": obj.content,
                # "project": obj.project,
                # "sprint": obj.sprint,
                "msgtype": obj.msgtype
            }
        else:
            raise IsNotExist(title='没有该名字的模版',detail=f'没有名字为【{name}】的模版')
