from flask import Flask
from app.dashboard.routes import bp_dashboard
from app.users.routes import bp_users
from app.project.routes import bp_project
import app.exceptions as app_exception
from app.extensions import db, migrate, bcrypt, login_manager
import os


def register_blueprints(app):
    app.register_blueprint(blueprint=bp_dashboard)
    app.register_blueprint(blueprint=bp_users)
    app.register_blueprint(blueprint=bp_project)

def register_error_handlers(app):
    app.register_error_handler(404, app_exception.page_not_found)

app = Flask(
    import_name=__name__,
    static_folder='static',
    template_folder='templates'
)


BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASEDIR, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object("config.DevConfig")

register_blueprints(app=app)

register_error_handlers(app=app)

bcrypt.init_app(app=app)

login_manager.init_app(app=app)

db.init_app(app=app)

from app.users.models import User

migrate.init_app(app=app, db=db)