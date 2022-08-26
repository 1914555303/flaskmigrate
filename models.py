# models.py
from ext import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT
from enum import IntEnum


# 创建ORM模型类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    # addresses = db.relationship('Address', backref='user')
    password = db.Column(db.String(100),nullable=False)


class Category(db.Model):
    """分类模型
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    icon = db.Column(db.String(128), nullable=True)
    post = db.relationship('Post', backref='category', lazy=True)
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, )  # 创建时间
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # 更新时间


class PostPublishType(IntEnum):
    """ 文章发布类型
    """
    draft = 1    # 草稿
    show = 2     # 发布

# 多对多关系帮助器表
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
)


class Post(db.Model):
    """文章模型
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.String(200), nullable=True)        # 文章简介
    has_type = db.Column(db.Enum(PostPublishType), server_default='show', nullable=False)  # 文章类型（草稿, 发布）
    # 一对多关系
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  #归属分类id
    content = db.Column(LONGTEXT, nullable=False)
    # 多对多关系
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('post', lazy=True))

    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, )  # 创建时间
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # 更新时间

class Tag(db.Model):
    """ 文章标签
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, )  # 创建时间
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # 更新时间

class Comments(db.Model):
    """评论
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(db.Integer, nullable=False)
    comment_content = db.Column(LONGTEXT, nullable=False)
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # 创建时间