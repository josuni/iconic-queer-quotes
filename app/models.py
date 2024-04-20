from flask_login import UserMixin
from datetime import datetime

from . import db
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64))
    quote = db.Column(db.String(2000))
    tags = db.Column(db.String(64))
    creation_time = db.Column(db.DateTime, default=datetime.now(), index=True)
    
class Submission(db.Model):
    __tablename__ = "submissions"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64))
    quote = db.Column(db.String(2000))
    tags = db.Column(db.String(64))
    creation_time = db.Column(db.DateTime, default=datetime.now(), index=True)
    

