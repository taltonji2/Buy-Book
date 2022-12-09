from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, PasswordField, validators, BooleanField
from flask_sqlalchemy import SQLAlchemy
import my_secrets
import pymysql

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(my_secrets.dbuser, my_secrets.dbpass, my_secrets.dbhost, my_secrets.dbname)

app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperSecretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = conn
db = SQLAlchemy(app)

# db Models
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "id: {0} | username: {1} | password: {2}".format(self.id, self.username, self.password)


class Bibliography(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))
    description = db.Column(db.String(500))
    publisher = db.Column(db.String(100))
    publication_year = db.Column(db.Integer)
    page_count = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    rating = db.Column(db.Integer)


class Book (db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    bibliography_id = db.Column(db.Integer, db.ForeignKey('bibliography.id'), nullable=False)


class Ownership (db.Model):
    __tablename__ = 'ownership'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Forms
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField(label='Password', validators=[validators.Length(min=6, max=10), validators.EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = StringField(label='Password confirm', validators=[validators.Length(min=6, max=10)])

# Routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/")
def index():
    data = "hello"
    return render_template("index.html", data=data)


if __name__ == '__app__':
    app.run(debug=True)



