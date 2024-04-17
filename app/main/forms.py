from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(),Length(min=8, max=32)])
    password = StringField('Password:', validators=[DataRequired(),Length(min=8, max=32)])
    submit = SubmitField('Admin Login')

class SignUpForm(FlaskForm):
    admin_key = StringField('Admin Key:', validators=[DataRequired(), Length(min=8, max=32)])
    username = StringField('Username:', validators=[DataRequired(),Length(min=8, max=32)])
    password = StringField('Password:', validators=[DataRequired(),Length(min=8, max=32)])
    confirm_password = StringField('Confirm Password:', validators=[DataRequired(),Length(min=8, max=32)])
    submit = SubmitField('Admin Sign Up')
