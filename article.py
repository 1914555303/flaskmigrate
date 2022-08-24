from flask import Blueprint
from flask import request, render_template
from models import Post

articles = Blueprint('aticles', __name__, url_prefix='/article')


@articles.route('')
def article():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.add_date).paginate(page, per_page=10, error_out=False)
    post_list = pagination.items
    return render_template('article.html', post_list=post_list, pagination=pagination)

