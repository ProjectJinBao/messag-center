from service.svc_sendmsg import svc_template_sendmsg,svc_sendmsg
from utils.exception_handle import IsExist, DefalutError,IsNotExist,NotMatch

def send_template_robot(body):
    content_name = body.get("content_name")
    robot_key = body.get("robot_key")
    svc_template_sendmsg(content_name=content_name, robot_key=robot_key)
    return {"title":"发送信息成功"}, 200


def send_robot(body):
    content = body.get("content")
    msgtype = body.get("msgtype")
    robot_key = body.get("robot_key")
    svc_sendmsg(content, robot_key, msgtype)
    return {"title":"发送信息成功"}, 200