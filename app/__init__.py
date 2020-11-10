from flask import Flask
#将Flask类的实例，赋值给名为app的变量，这个实例成为app包的成员
app = Flask(__name__)
#__name__打印的是那个包或者模块在使用我

from app import routes