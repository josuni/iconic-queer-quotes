from flask_login import UserMixin

from . import db
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))