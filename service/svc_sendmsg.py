# coding=utf-8
from database.db_sendmsg import db_sendmsg
from utils.search_jira import search_jira
from utils.qy_weixin_robot import QYWX_Robot
from utils.exception_handle import IsNotExist
from utils.content_handle import ContentHandle

# def svc_template_sendmsg(content_name, robot_key):
#     '''
#     已数据库中存在的content模版发送消息
#     :param content_name: 数据库中存储的模版名称（唯一）
#     :param robot_key: 发送的机器人key
#     :return:
#     '''
#
#     #获取发送url和conten
#     rsl=db_sendmsg(content_name = content_name, rel_key = robot_key)
#     # post_url = rsl.get("url")
#     content1 = rsl.get("content")
#     key = robot_key
#     msgtype = rsl.get("msgtype")
#     if msgtype == "text":
#         QYWX_Robot(key).send_text(content1)
#     elif msgtype == "markdown":
#         content = ContentHandle().conten_handle_template(content1)
#         QYWX_Robot(key).send_markdown(content)
#     elif msgtype == "images":
#         QYWX_Robot(key).send_markdown(content1)
#     elif msgtype == "news":
#         QYWX_Robot(key).send_markdown(content1)
#     else:
#         raise IsNotExist(title='不支持该格式的消息', detail=f'不支持【{msgtype}】的格式')

def svc_sendmsg(body):
    '''
    直接发送消息（content未存储在数据库中）
    :param content: 发送内容
    :param robot_key: 机器人key
    :param msgtype: 内容类型，markdown、text、image，news
    :return:
    '''
    print(body)
    for send in body:

        type = send.get("type")
        content = send.get("content")
        msgtype = send.get("msgtype")
        key = send.get("key")
        for k in key:
            if msgtype == "text":
                QYWX_Robot(k,type).send_text(content)
            elif msgtype == "markdown":
                QYWX_Robot(k,type).send_markdown(content)
            elif msgtype == "images":
                print("=====")
                QYWX_Robot(k,type).send_image(remote_url = content )
            elif msgtype == "news":
                QYWX_Robot(k,type).send_news(content)
            else:
                print("没有该格式内容")
