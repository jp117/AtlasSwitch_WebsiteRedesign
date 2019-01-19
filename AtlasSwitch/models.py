from AtlasSwitch import db, login_manager
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
    name = db.Column(db.String(30))
    access_level = db.Column(db.String(15))
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, email, password, access_level):
        self.name = name
        self.access_level = access_level
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Email {self.email} and access level is {self.access_level}'


class Quote(db.Model):

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


class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, text):
        self.text = text


class PandS(db.Model):
    __tablename__ = 'pands'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
