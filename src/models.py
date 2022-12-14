from src import db, login_manager, app
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


books_users_table = db.Table('books_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False),
    db.PrimaryKeyConstraint('user_id', 'book_id')
)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    picture = db.Column(db.String(64),nullable=False,default="default_profile.png")
    books = db.relationship('Book', 
        secondary=books_users_table, 
        backref="speculators", 
        )
    
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password (self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"


class Book (db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    users = db.relationship("User", secondary=books_users_table, backref="readers")
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self) -> str:
        return f"Book ID: {self.id}"




