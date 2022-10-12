from flask_wtf import FlaskForm
from app.users.models import User
from wtforms import StringField, PasswordField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class SignUpForm(FlaskForm):
    
    username = StringField(
        label='Username',
        validators=[
            DataRequired(message="Username Is Required!"),
            Length(min=8, max=30, message="Length Must Be Between 8 To 30!")
        ]
    )
    
    email = StringField(
        label='Email Address',
        validators=[
            DataRequired(message="Email Address Is Required!"),
            Email(message="Email Address Is Not Valid!")
        ]
    )
    
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message="Password Is Required!"),
            Length(min=8, max=30, message="Password Length Must Be Between 8 To 30!")
        ]
    )
    
    confirm_password = PasswordField(
        label='Confirm Password',
        validators=[
            DataRequired(message="Confirm Password Is Required!"),
            Length(min=8, max=30, message="Confirm Password Length Must Be Between 8 To 30!"),
            EqualTo('password')
        ]
    )
    
    avatar = FileField(
        label='Upload Avatar',
        validators=[
            DataRequired(message="Avatar Is Required!"),
        ]
    
    )
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(message="Username Is Already Taken!")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(message="Email Address Is Already Taken!")


class SignInForm(FlaskForm):
    
    username = StringField(
        label='Username',
        validators=[
            DataRequired(message="Username Is Required!"),
            Length(min=8, max=30, message="Length Must Be Between 8 To 30!")
        ]
    )
    
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired(message="Password Is Required!"),
            Length(min=8, max=30, message="Password Length Must Be Between 8 To 30!")
        ]
    )
    
    remember = BooleanField(
        label='Remember Me!'
    )