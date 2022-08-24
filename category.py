from flask import Blueprint
from flask import request, render_template
from models import Category

categorys = Blueprint('categorys', __name__, url_prefix='/category')

@categorys.route('')
def category():
    page = request.args.get('page', 1, type=int)
    pagination = Category.query.order_by(-Category.add_date).paginate(page, per_page=10, error_out=False)
    category_list = pagination.items
    print(page)
    print(pagination)
    print(category_list)
    return render_template('category.html', category_list=category_list, pagination=pagination)

