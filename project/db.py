from .settings import *
import flask_sqlalchemy, flask_migrate
import os

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)
migrate_path = os.path.abspath(os.path.join(__file__, '..', 'migrations'))
MIGRATE = flask_migrate.Migrate(
    app = project,
    db = DATABASE,
    directory = migrate_path
)