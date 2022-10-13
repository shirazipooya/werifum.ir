from flask_wtf import FlaskForm
from app.project.models import Project
from wtforms import StringField, PasswordField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class CreateProjectForm(FlaskForm):
    
    title = StringField(
        label='عنوان پروژه',
        validators=[
            DataRequired(message="عنوان پروژه | پروپوزال را وارد کنید!"),
            Length(min=5, max=300, message="Length Must Be Between 5 To 300!")
        ]
    )
    
    status = StringField(
        label='وضعیت پروژه',
        validators=[
            DataRequired(message="وضعیت پروژه | پروپوزال را وارد کنید!"),
            Length(min=5, max=100, message="Length Must Be Between 5 To 100!")        ]
    )
    
    organization = StringField(
        label='کارفرمای پروژه',
        validators=[
            DataRequired(message="کارفرمای پروژه | پروپوزال را وارد کنید!"),
            Length(min=5, max=100, message="Length Must Be Between 5 To 100!")        ]
    )
    
    person = StringField(
        label='مجری پروژه',
        validators=[
            DataRequired(message="مجری پروژه | پروپوزال را وارد کنید!"),
            Length(min=5, max=100, message="Length Must Be Between 5 To 100!")        ]
    )