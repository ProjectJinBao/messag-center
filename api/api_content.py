from utils.exception_handle import IsExist, DefalutError,IsNotExist
from service.svc_content import svc_create_content,svc_get_content,svc_update_content,svc_delete_content
import connexion
def create_content(body):
    try:
        svc_create_content(body)
        return 200
    except IsExist as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}', type=f'{e.type}')
    except Exception as e:
        raise DefalutError(title=f'未知错误',detail=f"{e}")

def get_content():
    try:
        return svc_get_content(),200
    except Exception as e:
        raise DefalutError(title=f'未知错误',detail=f"{e}")

def update_content(name, body):
    try:
        svc_update_content(name, body)
        return 200
    except IsNotExist as e:
        raise DefalutError(title=f"{e.title}", detail=f"{e.detail}", type=f'{e.type}')
    except Exception as e:
        raise DefalutError(title=f'未知异常', detail=f'{e}')

def delete_content(name):
    try:
        svc_delete_content(name)
        return 200
    except IsNotExist as e:
        raise DefalutError(title=f'{e.title}', detail=f'{e.detail}')
    except Exception as e:
        raise DefalutError(title="未知异常", detail=f'{e}')