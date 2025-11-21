import flask_login
from .settings import project
from home_app.models import User

project.secret_key='superdupermegaultra_secret_key'

login_manager=flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)