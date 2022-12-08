from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from decouple import config

config.encoding = 'cp1251'

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = config('DATABASE_URL')

db = SQLAlchemy(app)
# db Models
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Bibliography(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50))
    description = db.Column(db.String(500))
    publisher = db.Column(db.String(100))
    publication_year = db.Column(db.Integer(4))
    page_count = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    rating = db.Column(db.Integer)


class book (db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    bibliography_id = db.Column(db.Integer, db.ForeignKey('bibliography.id'), nullable=False)


class ownership (db.Model):
    __tablename__ = 'ownership'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'), nullable=False)

class wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'), nullable=False)



# @app.route('/')
# def index():


# # localhost:5000/user/tim
# @app.route('/user/<name>')
# def user(name):


# @app.route('/login', methods=['POST'])
# def login():


if __name__ == '__app__':
    app.run(debug=True)



