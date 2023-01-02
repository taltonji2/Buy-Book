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
    return render_template('books.html')


auth = Blueprint('auth', __name__)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

@auth.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    
        
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            time.sleep(1)
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
            time.sleep(1)
            flash("Successfully registered!")
            return redirect(url_for("users.login"))
    return render_template('register.html', form=form)

@auth.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
    else:
        return redirect(url_for('main.profile'))

    return render_template('login.html', form=form)

@auth.route('/account', methods=["GET", "POST"])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.username.data
        db.session.commit()
        return redirect(url_for('users.account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename="profile_pics/"+current_user.profile_image)
    return render_template("account.html", profile_image=profile_image, form=form)

@auth.route('/<username>')
def user_books(username):
    page = request.args.get("page",1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    books = Book.query.filter_by(owner=user).order_by(Book.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_books.html', books=books, user=user)