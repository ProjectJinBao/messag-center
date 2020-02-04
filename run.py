
import connexion
from database.mysql_conn import db
from database.db_info import Info
from database.db_content import Content
import sys
from utils.exception_handle import DefalutError

# import jsonpath
# print(jsonpath.jsonpath(d, 'stu_info.[0].id'))

if __name__ == '__main__':

    db.generate_mapping(create_tables=True)  # 创建表,实体类的映射关系,这种映射关系非常重要,pony在启动项目时会检查整个项目的所有实体类的映射关系是否正确。
    app = connexion.FlaskApp(__name__, port=8888, specification_dir='openapi/')
    app.add_api('openapi.yaml')

    #拦截器在请求之前进行判断
    @app.app.before_request
    def before():
        print(connexion.request.headers)
        if connexion.request.headers.get('Authorization') == 'NDX':
            pass
        else:
            raise DefalutError(title='验证失败')

    app.run(host='0.0.0.0', debug=True)



