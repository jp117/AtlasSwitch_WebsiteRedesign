from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Required
import datetime


class NewQuote(FlaskForm):
    jobname = StringField('Job Name')
    jobaddress = StringField('Job Address')
    amount = IntegerField('Amount', validators=[DataRequired()])
    followdate = DateField('Follow Up Date', validators=[DataRequired()],
                           default=datetime.date.today() + datetime.timedelta(days=7))
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit')
