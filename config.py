import os

class Config:
    
    BASE_DIR = os.path.abspath(
        path=os.path.dirname(p=__file__)
    )
    
    CSRF_ENABLED = True
    
    CSRF_SESSION_KEY = "0bcb9b4c5d6e9377b91d4953cd613dd92c0ad7c63a6a1395705dd799204aa2ec"
    
    SECRET_KEY = "249246568a937ad5c7066a34f64f9089ad52cea15b3fbff0bcd2e56589ba6c52"


class ProdConfig(Config):
    
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = ...
    
    


class DevConfig(Config):
    
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(Config.BASE_DIR, "app.db")