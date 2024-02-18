from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[
                        Email(message='input correct email')])
    password = PasswordField('Password', validators=[
                             Length(min=6, max=20),
                             EqualTo('password_confirm',
                                     message='password must match')])
    password_confirm = PasswordField('Repeat password',
                                     validators=[DataRequired(),
                                                 Length(min=6, max=20)])
    submit = SubmitField('Ok')


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[
                        Email(message='input correct email')])
    password = PasswordField('Password', validators=[
                             Length(min=6, max=20)])
    submit = SubmitField('Ok')
