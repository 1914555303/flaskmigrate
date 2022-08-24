from flask import Blueprint
from flask import render_template, request, url_for, redirect, session
from models import User, Category, Post

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/login',  methods=['GET', 'POST'])
def loginpage():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']

    user = User.query.filter(User.username == username).first()
    # pwd = user.password
    print(user)

    if user is None:
        errno = '用户名或密码错误！'
        return render_template('login.html', errnos=errno)
    else:
        if user.username == username and user.password == password:
            session['id'] = user.id
            session['username'] = user.username
            # return render_template('loginsuccess.html', username=username)
            return redirect(url_for('zhuye'))
        else:
            errno = '用户名或密码错误！'
            return render_template('login.html', errnos=errno)
