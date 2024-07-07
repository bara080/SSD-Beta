from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime)
    
    def get_id(self):
        return self.user_id
