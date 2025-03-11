from database import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True, nullable=False)
    
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    create_date = db.Column(db.String(100), nullable=False)
    
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
