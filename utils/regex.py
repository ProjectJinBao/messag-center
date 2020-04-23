#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
from utils.exception_handle import NotMatch,DefalutError


#正在匹配，search匹配key=的位置，span()返回一个元组类型,获取url中的key
def re_search(url, type):
    if type == "WeChat":
        result = re.search('key=', url)
        if result:
            key = url[re.search('key=', url).span()[1]:]
            return key
        else:
            raise NotMatch(title='url地址异常',detail=f'{url}缺少参数key')
    elif type == "DingDing":
        result = re.search('access_token=', url)
        if result:
            key = url[re.search('access_token=', url).span()[1]:]
            return key
        else:
            raise NotMatch(title='url地址异常', detail=f'{url}缺少参数access_token=')
    else:
        raise NotMatch(title='type错误', detail=f'{type}不存在')


