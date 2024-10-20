from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON  # Use this for JSON fields in SQLite

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    mobile = db.Column(db.String(15), nullable=False)

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    split_type = db.Column(db.String(50), nullable=False)
    participants = db.Column(JSON, nullable=False)  # Storing as JSON
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

