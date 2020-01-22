import pony.orm
from  database.mysql_conn import db
import datetime
from pony.orm import (Json, PrimaryKey, Required, db_session, select, desc, Set, get, Optional)
from utils.exception_handle import IsExist, IsNotExist

class Content(db.Entity):
    _table_ = 'content'
    id = PrimaryKey(int, auto=True)
    msgtype = Required(str, 30, default="text")
    name = Required(str, 50, default="未知")
    content = Optional(Json)
    isdelete = Required(bool, default='false')

