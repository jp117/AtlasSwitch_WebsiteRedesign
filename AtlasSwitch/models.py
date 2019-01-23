from AtlasSwitch import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime


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
    date = db.Column(db.DateTime, nullable=False, default=datetime.date.today())

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


class FollowUp(db.Model):
    __tablename__ = 'followup'

    id = db.Column(db.Integer, primary_key=True)
    salesman = db.Column(db.String(64), nullable=False)
    jobname = db.Column(db.String(128))
    job_address = db.Column(db.String(128))
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.date.today())
    nextfollowup = db.Column(db.DateTime, nullable=False, default=datetime.date.today() + datetime.timedelta(days=7))
    notes = db.Column(db.Text)
    stoptracking = db.Column(db.Boolean, nullable=False, default=False)
    closed = db.Column(db.String(64))


class Customer(db.Model):

    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    street = db.Column(db.String(128))
    city = db.Column(db.String(128))
    state = db.Column(db.String(32))
    zipcode = db.Column(db.Integer)
    phone = db.Column(db.String(11))
    revenue = db.Column(db.Integer)
    custclass = db.Column(db.String(32), nullable=False)
    notes = db.Column(db.Text)
