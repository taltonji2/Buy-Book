
class Book (db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    bibliography_id = db.Column(db.Integer, db.ForeignKey("bibliography.id"), nullable=False)