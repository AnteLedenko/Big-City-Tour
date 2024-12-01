# Here again creating all necessary imports initializing SQLAlchemy and then creating three
# classes thta mop database tables and defining their relationships

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False ,unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text, nullable=False)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship('Review', back_populates='created_by')

    
    def get_id(self):
        """A loader method for flask_login"""
        return str(self.user_id)


class Tour(db.Model):
    __tablename__ = 'tours'
    tour_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False) 
    tour_name = db.Column(db.String(200))
    tour_content = db.Column(db.Text)

    reviews = db.relationship('Review', back_populates='tour')


class Review(db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.tour_id'))
    review_content = db.Column(db.Text)

    created_by = db.relationship('User', back_populates='reviews')
    tour = db.relationship('Tour', back_populates='reviews')


