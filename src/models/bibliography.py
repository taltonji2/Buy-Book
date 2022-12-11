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


