from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , SelectField , DateField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo


class SignupForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(),Length(min=2, max=30)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        "Gender",
        choices=["Male","Female","others"],
        validators=[Optional()]
    )
    dob = DateField(
        'Date of Birth',
        validators=[Optional()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(),Length(min=5, max=25)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(),Length(min=5,max=25),EqualTo('password',message='Passwords must match')]

    )
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField(
        'Email',
        validators=[DataRequired(),Email()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(),Length(min=5, max=25)]
    )
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Log In')