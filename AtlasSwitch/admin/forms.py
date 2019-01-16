from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Required


class HistoryForm(FlaskForm):
    text = TextAreaField('History', validators=[DataRequired()])
    submit = SubmitField('Update History')
