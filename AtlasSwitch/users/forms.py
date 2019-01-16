from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Required
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from AtlasSwitch.models import User


accessChoices = [('', ''), ('admin', 'admin'), ('sales', 'sales'), ('engineer', 'engineer')]


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class NewUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    access_level = SelectField('Access Level', choices=accessChoices, validators=[Required()])
    submit = SubmitField('Create New User')
