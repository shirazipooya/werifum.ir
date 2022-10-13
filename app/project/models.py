from app.models import BaseModel
from app.extensions import db, login_manager


class Project(BaseModel):
    
    title = db.Column(db.String(300), unique=False, nullable=False)
    status = db.Column(db.String(100), unique=False, nullable=False)
    organization = db.Column(db.String(100), unique=False, nullable=False)
    person = db.Column(db.String(100), unique=False, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.id}, {self.title})"