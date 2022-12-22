from flask import render_template, request, Blueprint

core = Blueprint('core', __name__,)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/signup')
def signup():
    return render_template('signup.html')

@core.route('/books')
def books():
    return render_template('books.html')
