from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from src import db
from src.models import User, Book
from src.forms.users import RegistrationForm, LoginForm, UpdateUserForm
from src.picture_handler import add_profile_pic
import time

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/books')
def books():
    return render_template('books.html', books=Book.query.all())


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash("Email already registered!")
            return render_template('register.html', form=form)
        else:
            user = User(
                email=form.email.data, 
                username=form.username.data, 
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            flash("Successfully registered!")
            return redirect(url_for("auth.login"))
    return render_template('register.html', form=form)

@auth.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash('Check login credentials, try again')
            return redirect(url_for('auth.login'))

        if user.check_password(form.password.data):
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')
            print("here")
            if next == None or not next[0]=="/":
                next = url_for("main.index")
            
            return redirect(next)
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/account', methods=["GET", "POST"])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            print(pic)
            current_user.picture = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User Account Updated")
        return redirect(url_for('auth.account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename="profile_pics/"+current_user.picture)
    return render_template("account.html", profile_image=profile_image, form=form)

@auth.route('/<username>')
def user_books(username):
    user = User.query.filter_by(username=username).first_or_404()
    query = Book.query.join(Book, User.books)
    books = query.order_by(Book.title).all()
    return render_template('user_books.html', books=books, user=user)