#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re


#正在匹配，search匹配key=的位置，span()返回一个元组类型,获取url中的key
def re_search(url):
    key = url[re.search('key=', url).span()[1]:]
    return key

