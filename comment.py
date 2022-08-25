from flask import Blueprint
from flask import request, render_template, redirect, url_for
from models import Post
from ext import db

comments = Blueprint('comments', __name__, url_prefix='/comment')

@comments.route('/<posts_id>', methods=['GET', 'POST'])
def comment(posts_id):
    print(posts_id)
    return render_template('comment.html')
