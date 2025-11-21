import flask_login
from project.db import DATABASE as DB

class User(DB.Model, flask_login.UserMixin):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String)
    password = DB.Column(DB.String)
    is_admin = DB.Column(DB.Boolean , default = False)
    def __str__(self):
        return f"<User: {self.name}, id - {self.id}>"

