from flask import Flask, render_template, request, url_for, redirect, flash ,session
from ext import db
import config
from models import User, Category, Post
import models
from admin import admin
from user import user
from category import categorys
from article import articles
from comment import comments

# 目的：练习Flask-Migrate模块的使用
# 安装依赖：  pip install flask-migrate
# 其他依赖：
# pip install pymysql
# pip install SQLAlchemy
# pip install flask-sqlalchemy
# pip install flask-script

# 迁移命令
# 1.python manage.py db init
# 2.python manage.py db migrate
# 3.python manage.py db upgrade

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(config)  # 载入config.py中的配置信息
#
#     db.init_app(app)  # app绑定数据库db
#
#     return app

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)

# 注册蓝图
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(categorys)
app.register_blueprint(articles)
app.register_blueprint(comments)

@app.route('/index')
def index():

    return render_template("index.html")


# @app.route('/login',  methods=['GET', 'POST'])
# def loginpage():
#     if request.method == 'GET':
#         return render_template('login.html')
#
#     username = request.form['username']
#     password = request.form['password']
#
#     user = User.query.filter(User.username == username).first()
#     # pwd = user.password
#     print(user)
#
#     if user is None:
#         errno = '用户名或密码错误！'
#         return render_template('login.html', errnos=errno)
#     else:
#         if user.username == username and user.password == password:
#             session['id'] = user.id
#             session['username'] = user.username
#             # return render_template('loginsuccess.html', username=username)
#             return redirect(url_for('zhuye'))
#         else:
#             errno = '用户名或密码错误！'
#             return render_template('login.html', errnos=errno)

# 主页
@app.route('/zhuye')
def zhuye():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.add_date).paginate(page, per_page=2, error_out=False)
    post_list = pagination.items
    post_num = Post.query.count()


    return render_template('loginsuccess.html', post_list=post_list, pagination=pagination, post_num=post_num)





# 注册
@app.route('/register', methods=['GET', 'POST'])
def registerpage():
    if request.method == 'GET':
        return render_template('register.html')
    nusername = request.form['username']
    npassword = request.form['password']
    npassword1 = request.form['password1']

    if nusername == '' or npassword1 == '' or npassword == '':
        errno = '用户名或密码不能为空！'
        print("!!!!!")
        return render_template('register.html', errno=errno)
    if npassword !=npassword1:
        errno = '两次密码输入不一致！'
        return render_template('register.html', errno=errno)
    nuser = User.query.filter(User.username == nusername).first()
    print(nuser)

    if nuser is None:
        user1 = User(username=nusername, password=npassword)
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('admin.loginpage'))
        # return render_template('login.html')

    else:
        errno = '用户名已存在！'
        return render_template('register.html', errno=errno)

# 注销
@app.route('/logout')
def logoutpage():
    session.clear()
    return redirect(url_for('index'))



# @app.route('/category')
# def category():
#     page = request.args.get('page', 1, type=int)
#     pagination = Category.query.order_by(-Category.add_date).paginate(page, per_page=10, error_out=False)
#     category_list = pagination.items
#     print(page)
#     print(pagination)
#     print(category_list)
#     return render_template('category.html', category_list=category_list, pagination=pagination)


# @app.route('/article')
# def article():
#     page = request.args.get('page', 1, type=int)
#     pagination = Post.query.order_by(Post.add_date).paginate(page, per_page=10, error_out=False)
#     post_list = pagination.items
#     return render_template('article.html',post_list=post_list, pagination=pagination)




    # return render_template('login.html')




if __name__ == '__main__':
    # app = create_app()
    app.run()