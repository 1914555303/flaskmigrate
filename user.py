from flask import Blueprint
from flask import render_template, request, url_for, redirect, session
from models import User, Category, Post

user = Blueprint('user', __name__ , url_prefix='/user')


