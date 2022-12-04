from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from decouple import config

config.encoding = 'cp1251'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite::///users.db'
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.debug = True

db = SQLAlchemy(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = config('DATABASE_URL')

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name

# Form Class
class NameForm(FlaskForm):
    name = StringField("What\'s your name", validators=[DataRequired()])
    submit = SubmitField("Submit")



# localhost:5000/
@app.route('/')
def index():
    return render_template("index.html")

# localhost:5000/user/tim
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",
        name = name,
        form = form)

# Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




