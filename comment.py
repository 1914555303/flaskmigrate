from flask import Blueprint
from flask import request, render_template, redirect, url_for, session
from models import Post, Comments
from ext import db


comments = Blueprint('comments', __name__, url_prefix='/comment')

@comments.route('', methods=['GET', 'POST'])
def comment():
    print(session.get('username'))
    posts_id = request.values.get('posts_id')
    if request.method == 'POST':
        # comments1 = Comments.query.filter_by(article_id=posts_id).all()
        comments2 = db.session.query(Comments.comment_content, Comments.add_date).filter(Comments.article_id==posts_id).all()
        post1 = Post.query.filter_by(id=posts_id).first()
        comment_content1 = request.form['content1']
        if comment_content1 == '':
            errno = '评论不可以为空！'
            return render_template('comment.html', post1=post1, comments1=comments2, post_id1=posts_id, errno=errno)

        comment2 = Comments( article_id=posts_id, comment_content=comment_content1)
        db.session.add(comment2)
        db.session.commit()
        return render_template('comment.html', post1=post1, comments1=comments2, post_id1=posts_id)

    comments2 = db.session.query(Comments.comment_content, Comments.add_date).filter(Comments.article_id == posts_id).all()
    # comments1 = Comments.query.filter_by(article_id=posts_id).all()
    post1 = Post.query.filter_by(id=posts_id).first()
    return render_template('comment.html', post1=post1, comments1=comments2, post_id1=posts_id)

@comments.route('/add', methods=['GET', 'POST'])
def comment_add():
    if request.method == 'POST':
    #     print(post_id1)
    #     print(request.form['content1'])
    #     comment_content1 = request.form['content1']
    #     comment2 = Comments(article_id=post_id1, comment_content=comment_content1)
    #     db.session.add(comment2)
    #     db.session.commit()
    #     # return render_template('comment.html')
    #     # return redirect(url_for('comments.comment'))
    # print(request.form['content1'])
        print(request.args.get('post_id1'))
        pass



    return render_template('comment_add.html')

