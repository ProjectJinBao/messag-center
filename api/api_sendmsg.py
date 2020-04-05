from service.svc_sendmsg import svc_template_sendmsg,svc_sendmsg
from utils.exception_handle import IsExist, DefalutError,IsNotExist,NotMatch,FormatTypeError

def send_template_robot(body):
    try:
        content_name = body.get("content_name")
        robot_key = body.get("robot_key")
        svc_template_sendmsg(content_name=content_name, robot_key=robot_key)
        #一个return返回多个值 响应信息，状态码，响应头：元组形式 [("test","11")]或者json格式{"test":"11"}
        return {"title":"发送信息成功"}, 200,
    except FormatTypeError as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}', type=f'{e.type}')
    except Exception as e:
        raise DefalutError(title=f'未知异常', detail=f'{e}')

def send_robot(body):
    try:
        content = body.get("content")
        msgtype = body.get("msgtype")
        robot_key = body.get("robot_key")
        svc_sendmsg(content, robot_key, msgtype)
        return {"titile": "发送消息成功"}, 200
    except IsNotExist as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}', type=f'{e.type}')
    except Exception as e:
        raise DefalutError(title=f'未知异常', detail=f'{e}')
