FROM python:3.7

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >> /etc/timezone

ADD . .
WORKDIR .

RUN pip install -r requirements.txt

CMD ["python", "/code/run.py"]