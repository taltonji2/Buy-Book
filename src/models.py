from src import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    picture = db.Column(db.String(64),nullable=False,default="default_profile.png")
    books = db.relationship('Books', backref='author', lazy=True)

    
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password (self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"


class Book (db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    
    users = db.relationship(User)
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self) -> str:
        return f"Book ID: {self.id}"
