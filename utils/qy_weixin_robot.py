import requests
import base64
import hashlib



class QYWX_Robot(object):
    def __init__(self, key):
        self.url ='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key

        self.headers = {
            'Content-Type': 'application/json'
        }


    def send(self, payload):
        rs = requests.post(self.url, headers = self.headers, json=payload)
        print(self.url, payload)
        assert rs.status_code == 200
        return True


    def send_text(self, content):
        """
        文本类型
        :param content:
        :return:
        """
        payload = {
            'msgtype': 'text',
            'text': {
                'content': content,
                # 'mentioned_list': ['@all'],  # Optional
                # 'mentioned_mobile_list': ['@all']  # Optional
            }
        }
        self.send(payload)

    def send_markdown(self, content: str):
        """
        Markdown 类型
        :param content:
        :return:
        """
        payload = {
            'msgtype': 'markdown',
            'markdown': {
                'content': content,
            }
        }
        # payload = payload.encode("utf-8")
        self.send(payload)


    def send_image(self, local_file=None, remote_url=None):
        """
        图片类型
        :param local_file: local file path
        :param remote_url: image url
        :return:
        """
        if local_file:
            with open(local_file, 'rb') as f:
                image_content = f.read()
        elif remote_url:
            image_content = requests.get(remote_url).content
        else:
            raise Exception('Need provide local_file: str or remote_url: str')
        image_base64 = base64.b64encode(image_content).decode('utf-8')
        md5 = hashlib.md5()
        md5.update(image_content)
        image_md5 = md5.hexdigest()
        payload = {
            'msgtype': 'image',
            'image': {
                'base64': image_base64,
                'md5': image_md5
            }
        }
        self._send(payload)


    def send_news(self, articles: list):
        """
        图文类型
        :param articles: [
            {
                'title': '',
                'description': '',  # Optional
                'url': '',
                'picurl': '',  # Optional
            }
        ]
        :return:
        """
        assert len(articles) <= 8, 'Only support 1-8 articles'
        for article in articles:
            assert article.get('title'), 'Need provide article title'
            assert article.get('url'), 'Need provide article url'
        payload = {
            'msgtype': 'news',
            'news': {
                'articles': articles
            }
        }
        self._send(payload)




            # # markdown格式数据
        # payload = json.dumps({
        #     "msgtype": "markdown",
        #     "markdown": {
        #         "content": f"DX DMP 2.3.0\n>* <font color=\"warning\">待修复：{new_num}</font>\n>* <font color=\"comment\">已修复：{fixed_num}</font>\n >* <font color=\"info\">已验证：{verified_num}</font>\n  "
        #                    ">* [JIRA链接](https://jira.daocloud.io/secure/RapidBoard.jspa?rapidView=305&projectKey=DX&view=detail&selectedIssue=DX-955&sprint=567)"
        #     }
        # })
        # payload = payload.encode("utf-8")
        # response = requests.request("POST", post_url, data=payload)