from app.models import BaseModel
from app.extensions import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(BaseModel, UserMixin):
    
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    avatar = db.Column(db.String(), unique=False, nullable=False, default='avatar.png')
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.id}, {self.username})"