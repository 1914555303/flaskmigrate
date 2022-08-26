from flask import Blueprint
from flask import request, render_template,redirect, url_for
from models import Post
from ext import db

articles = Blueprint('articles', __name__, url_prefix='/article')


@articles.route('')
def article():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.add_date).paginate(page, per_page=5, error_out=False)
    post_list = pagination.items
    return render_template('article.html', post_list=post_list, pagination=pagination)

@articles.route('/add', methods=['GET', 'POST'])
def article_add():
    if request.method == 'GET':
        return render_template('article_add.html')

    title = request.form['title']
    desc = request.form['desc']
    category = request.form['category']
    tag = request.form['tag']
    content = request.form['content']

    article1 = Post(title=title, desc=desc, category_id=category, content=content)
    db.session.add(article1)
    db.session.commit()
    errno = '文章添加成功'
    return render_template('article_add.html', errno=errno)

@articles.route('/edit/<post_id>', methods=['GET', 'POST'])
def article_edit(post_id):
    # print(post_id)
    if request.method == 'GET':
        post1 = Post.query.filter_by(id=post_id).first()
        return render_template('article_edit.html', post1=post1)

    post1 = Post.query.filter_by(id=post_id).first()

    print(request.form['title'])
    print(request.form['desc'])
    if request.form['title']=='' or request.form['desc']=='' or request.form['category']=='' or request.form['content']=='' or request.form['tag']=='':
        errno = '不可以为空！'
        return render_template('article_edit.html', errno=errno,post1=post1)

    post1.title = request.form['title']
    post1.desc = request.form['desc']
    post1.category_id = request.form['category']
    tag = request.form['tag']
    post1.content = request.form['content']

    db.session.commit()
    errno = '文章修改成功'

    return render_template('article_edit.html', errno=errno,post1=post1)

@articles.route('/delete/<post_id>', methods=['GET', 'POST'])
def article_delete(post_id):
    Post.query.filter(Post.id==post_id).delete()
    db.session.commit()
    return redirect(url_for('articles.article'))

