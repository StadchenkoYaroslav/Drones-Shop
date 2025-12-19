
import os

def migrate():
    migrate_path = os.path.abspath(os.path.join(__file__,'..','migrations'))
    if not os.path.exists(migrate_path):
        os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")