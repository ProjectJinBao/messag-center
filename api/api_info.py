from service.svc_info import svc_get_info,svc_creat_info,svc_put_info,svc_del_info
from utils.exception_handle import IsExist, DefalutError,IsNotExist,NotMatch


#获取企业微信机器人信息，接口/robot
def get_info():
    try:
        return svc_get_info(), 200
    except Exception as e:
        return {
            'title': '获取列表异常',
            'detail': f'{e}'
        },500
#上传机器人信息
def get_info_test():
    try:
        return svc_get_info(), 200
    except Exception as e:
        return {
            'title': '获取列表异常',
            'detail': f'{e}'
        },500
#上传机器人信息
def create_info(body):

    try:
        svc_creat_info(body)
        return {"title": "企业微信机器人信息上传成功"}, 200
    except IsExist as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}', type=f'{e.type}')
    except NotMatch as e:
        raise DefalutError(title=f'{e.title}',detail=f'{e.detail}')
    except Exception as e:
        raise DefalutError(title=f'未知异常', detail=f'{e}')
#更新机器人信息
def update_info(key, body):
    try:
        svc_put_info(key,body)
        return {"title": "更新信息成功"}, 200
    except IsNotExist as e:
        return {'title':f'{e.title}', 'detail': f'{e.detail}', 'type': f'{e.type}'},400
    except Exception as e:
        raise DefalutError(title=f'未知异常', detail=f'{e}')
#删除机器人信息
def delete_info(key):
    try:
        svc_del_info(key)
        return {"title": "删除成功"}, 200
    except IsNotExist as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}', type=f'{e.type}')
    except Exception as e:
        raise DefalutError(title=f'未知异常', detail=f'{e}')





