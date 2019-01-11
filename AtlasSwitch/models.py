from puppycompanyblog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


# Have to relook up what this does
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    access_level = db.Column(db.Integer)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Email {self.email}'


class ProductPage(db.model):

    __tablename__ = 'productpage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    text = db.Column(db.Text, nullable=False)


class Quote(db.model):

    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    quote_num = db.Column(db.Integer)
    revision_num = db.Column(db.Integer)
    job_name = db.Column(db.String(128))
    job_address = db.Column(db.String(128))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, quote_num, revision_num, job_name, job_address):
        self.quote_num = quote_num
        self.revision_num = revision_num
        self.job_name = job_name
        self.job_address = job_address


class PanelQuote(db.model):

    __tablename__ = 'panelquotes'
