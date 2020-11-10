from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()
#导入config配置文件
from config import Config
#将Flask类的实例，赋值给名为app的变量，这个实例成为app包的成员
app = Flask(__name__)
#__name__打印的是那个包或者模块在使用我
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])

#db对象是SQLAlchemy创建的数据库实例，表示应用使用的数据库，通过它可获得Flask-SQLAlchemy提供的所有功能
db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
#从app包中导入routes，models他将定义数据库的结构，
from app import routes,models