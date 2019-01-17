from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Required
from flask_wtf.file import FileField, FileAllowed


class HistoryForm(FlaskForm):
    text = TextAreaField('History', validators=[DataRequired()])
    submit = SubmitField('Update History')


class PandSForm(FlaskForm):
    image = FileField('Product Picture', validators=[FileAllowed(['jpg', 'png'])])
    name = StringField('Product Name', validators=[DataRequired()])
    text = TextAreaField('Description of Product or Service', validators=[DataRequired()])
    submitpands = SubmitField('Update Products and Services')
