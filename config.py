import os
import pymysql
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
	#需要数据库中创建该需要使用的数据库
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://root:root@127.0.0.1/db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False