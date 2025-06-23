from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique=True, nullable=False)
    email=db.Column(db.String(150), unique=True, nullable=False)
    password_hash=db.Column(db.String(150), nullable=False)
    expenses= db.relationship("Expense", backref="user")
    
    def __repr__(self):
        return f"<User {self.username}>"
    
class Expense(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    amount=db.Column(db.Float(),nullable=False)
    category=db.Column(db.String(100),nullable=False)
    note=db.Column(db.String(200))
    date=db.Column(db.Date, default=datetime.utcnow)
    user_id= db.Column(db.Integer, db.ForeignKey("user.id"))
    


