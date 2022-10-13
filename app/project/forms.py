from flask_wtf import FlaskForm
from app.project.models import Project
from wtforms import StringField, PasswordField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class CreateProjectForm(FlaskForm):
    
    title = StringField(
        label='عنوان',
        validators=[
            DataRequired(message="Title Is Required!"),
            Length(min=5, max=300, message="Length Must Be Between 5 To 300!")
        ]
    )
    
    status = StringField(
        label='وضعیت',
        validators=[
            DataRequired(message="Status Is Required!"),
            Length(min=5, max=100, message="Length Must Be Between 5 To 100!")        ]
    )
    
    organization = StringField(
        label='سازمان',
        validators=[
            DataRequired(message="Organization Is Required!"),
            Length(min=5, max=100, message="Length Must Be Between 5 To 100!")        ]
    )
    
    person = StringField(
        label='مجری',
        validators=[
            DataRequired(message="Person Is Required!"),
            Length(min=5, max=100, message="Length Must Be Between 5 To 100!")        ]
    )
    
    def validate_title(self, title):
        project = Project.query.filter_by(title=title.data).first()
        if project:
            raise ValidationError(message="This Project Is Already Submitted!")