from app import app
#两个路由
@app.route('/')
@app.route('/index')
#一个视图函数
def index():
    return "初始页"