from app import app
from flask import render_template
#两个路由
@app.route('/')
@app.route('/index')
#一个视图函数
def index():
    user = {'username':'dfs'}
    # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('index.html',title='home',name=user,posts=posts)