from database.db_sendmsg import db_sendmsg
from utils.search_jira import search_jira
from utils.qy_weixin_robot import QYWX_Robot

def svc_template_sendmsg(content_name, robot_key):

    #获取发送url和content
    rsl=db_sendmsg(content_name=content_name, robot_key=robot_key)
    # post_url = rsl.get("url")
    project = rsl.get("project")
    sprint = rsl.get("sprint")
    if project != "" or sprint != "":
        #获取jira中数据
        num = search_jira(project, sprint)
        new_num = num.get("new_num")
        fixing_num = num.get("fixing_num")
        fixed_num = num.get("fixed_num")
        verified_num = num.get("verified_num")
        content = rsl.get("content")
    else:
        content = rsl.get("content")

    key = robot_key
    msgtype = rsl.get("msgtype")
    if msgtype == "text":
        QYWX_Robot(key).send_text(content)
    elif msgtype == "markdown":
        QYWX_Robot(key).send_markdown(content)
    elif msgtype == "images":
        QYWX_Robot(key).send_markdown(content)
    elif msgtype == "news":
        QYWX_Robot(key).send_markdown(content)
    else:
        print("没有该格式内容")

def svc_sendmsg(content, robot_key, msgtype):
    key = robot_key
    if msgtype == "text":
        QYWX_Robot(key).send_text(content)
    elif msgtype == "markdown":
        QYWX_Robot(key).send_markdown(content)
    elif msgtype == "images":
        QYWX_Robot(key).send_markdown(content)
    elif msgtype == "news":
        QYWX_Robot(key).send_markdown(content)
    else:
        print("没有该格式内容")