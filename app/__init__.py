from flask import Flask
#导入config配置文件
from config import Config
#将Flask类的实例，赋值给名为app的变量，这个实例成为app包的成员
app = Flask(__name__)
#__name__打印的是那个包或者模块在使用我
app.config.from_object(Config)
print(app.config['SECRET_KEY'])
#从app包中导入routes
from app import routes