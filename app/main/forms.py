from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms import HiddenField

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(),Length(min=8, max=64)])
    password = StringField('Password:', validators=[DataRequired(),Length(min=8, max=64)])
    submit = SubmitField('Admin Login')

class SignUpForm(FlaskForm):
    admin_key = StringField('Admin Key:', validators=[DataRequired(), Length(min=8, max=64)])
    username = StringField('Username:', validators=[DataRequired(),Length(min=8, max=64)])
    password = StringField('Password:', validators=[DataRequired(),Length(min=8, max=64)])
    confirm_password = StringField('Confirm Password:', validators=[DataRequired(),Length(min=8, max=64)])
    submit = SubmitField('Admin Sign Up')

class SubmitForm(FlaskForm):
    author = StringField('Author:', validators=[DataRequired(), Length(min=1, max=64)])
    quote = TextAreaField('Quote:', validators=[DataRequired(), Length(min=1, max=2000)])
    tags = StringField('Tags:', validators=[Length(min=0, max=64)])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    id = StringField('Id')
    approve = SubmitField('Approve')
    reject = SubmitField('Reject')
