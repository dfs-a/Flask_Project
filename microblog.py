from app import app,db
from app.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User':User,'Post':Post}

if __name__ == '__main__':
    print('运行成功')
    # u1 = User(username='susan',email='susan@example.com',password_hash='abcdefg')
    # u2 = User()
    app.run(host='0.0.0.0',port=5000,debug=True)