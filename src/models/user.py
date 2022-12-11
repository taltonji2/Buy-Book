from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    username = db.Column(
        db.String(25), 
        nullable=False
    )
    password = db.Column(
        db.String(50), 
        nullable=False
    )

def set_password(self, password):
    self.password = generate_password_hash(
        password,
        method='sha256'
    )

def check_password(self, password):
    return check_password_hash(
        self.password, 
        password
    )

def __repr__(self):
    return '<User {}>'.format(self.username)