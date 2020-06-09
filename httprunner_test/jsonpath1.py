body= {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

tobot_msg = [
  {
    "comment": "DMP测试报告",
    "create_time": "2020-01-19T11:41:37Z",
    "id": 1,
    "key": "ed02f420-63dd-4a45-8816-28c979795d5f",
    "name": "DX-DMP-冲刺看板",
    "type": "",
    "update_time": "",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ed02f420-63dd-4a45-8816-28c979795d5f"
  },
  {
    "comment": "NDX-Quality",
    "create_time": "2020-01-20T19:54:22Z",
    "id": 9,
    "key": "074e0adc-40a5-478a-a7f3-5fbc38c6bc2b",
    "name": "NDX-update",
    "type": "",
    "update_time": "2020-02-03T17:06:03Z",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=074e0adc-40a5-478a-a7f3-5fbc38c6bc2b"
  },
  {
    "comment": "",
    "create_time": "2020-02-05T12:05:17Z",
    "id": 10,
    "key": "ed02f420-63dd-4a45-8816-28c979795d00",
    "name": "ee",
    "type": "",
    "update_time": "2020-02-05T12:05:17Z",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ed02f420-63dd-4a45-8816-28c979795d00"
  },
  {
    "comment": "",
    "create_time": "2020-02-05T12:05:17Z",
    "id": 11,
    "key": "ed02f420-63dd-4a45-8816-28c99",
    "name": "ee",
    "type": "",
    "update_time": "2020-02-05T12:05:17Z",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ed02f420-63dd-4a45-8816-28c999795d00"
  },
  {
    "comment": "DMP测试报告",
    "create_time": "2020-04-22T21:25:01Z",
    "id": 12,
    "key": "ed012f420-63dd-4a45-8816-28c979795d5f",
    "name": "DX-DMP-冲刺看板",
    "type": "DingDing",
    "update_time": "",
    "url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?access_token=ed012f420-63dd-4a45-8816-28c979795d5f"
  }
]

l = {
  "detail": "name为【name】的模版已经存在",
  "status": 400,
  "title": "该名字的模版已经存在",
  "type": "IsExist"
}

import jsonpath
import json
# response = json.loads(json_body)
# test = jsonpath.jsonpath(tobot_msg, '$..')
# test2 = jsonpath.jsonpath(tobot_msg, 'content')

a = jsonpath.jsonpath(tobot_msg, '$..comment')
print(type(a),a)

print(body["store"])