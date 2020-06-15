import requests
def sum_status_code(content, expect_sum):
    """ sum status code digits
        e.g. 400 => 4, 201 => 3
    """
    c = content[0]
    ss = c["comment"]
    # sum_value = 0
    # for digit in str(status_code):
    #     sum_value += int(digit)
    print(ss)

    assert ss == expect_sum


def creat_name():
    # -*- coding:utf-8 -*-
    import uuid
    uuid_num = uuid.uuid1()
    onlyname =  str(uuid_num)
    return onlyname

def get_contetn_name():
    import pymysql
    db = pymysql.connect(
        host = '10.10.30.59',
        port= 3307,
        user = "root",
        password = "123456",
        db = "message_center")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql_query = "select name from content where isdelete is not True"
    cursor.execute(sql_query)
    # 使用 fetchone() 方法获取一条数据,类型为元组
    data = cursor.fetchone()

    # 关闭数据库连接
    db.close()
    return data[0]


def get_info(infoname):
    import pymysql
    db = pymysql.connect(
        host='10.10.30.59',
        port=3307,
        user="root",
        password="123456",
        db="message_center")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql_query = "select name from content where isdelete is not True"
    cursor.execute(sql_query)
    # 使用 fetchone() 方法获取一条数据,类型为元组
    data = cursor.fetchone()
    sql_query_robots = "selete key from info"
    cursor.execute(sql_query)
    key_r = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    if infoname == "content":
      return data[0]
    elif infoname == "key":
      return key_r[0]
    else:
      print("没有匹配的内容")

      import requests

def s_config1(author, name):
      h = {"Authorization": author}
      url = "http://10.8.1.244:8888/contents"
      body = {"msgtype": "text", "content": "jjjjji", "name": name}
      rs = requests.request("POST", url, headers=h, json=body)
      print("==================")

def s_config2(a, b):
    return a + b

def t_config1(author, name):
      h = {"Authorization": author}
      url = f"http://10.8.1.244:8888/contents/{name}"
      body = {"msgtype": "text", "content": "update", "name": name}
      rs = requests.request("PUT", url, headers=h, json=body)
      print("=======+++++++++")

def t_config2():
      y = 1 + 1


def delete_content(author, name):
    namestr = str(name)
    h = {"Authorization": author}
    url = f"http://10.8.1.244:8888/contents/{namestr}"
    print(url)
    rs = requests.request("DELETE", url, headers=h)

delete_content("NDX","xumin")

s_config2(1,2)
print(type(s_config2("yu","2")))