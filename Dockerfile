FROM python:3.7
MAINTAINER The CentOS <362639663@qq.com>

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >> /etc/timezone

ADD . .
WORKDIR .

RUN pip install -r requirements.txt

#指定容器启动后要干的事情
CMD ["python", "run.py"]