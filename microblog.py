from app import app
if __name__ == '__main__':
    print('运行成功')
    app.run(host='0.0.0.0',port=5000,debug=True)