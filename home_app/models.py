import flask_login
from project.db import DATABASE as DB

class User(DB.Model, flask_login.UserMixin):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String)
    password = DB.Column(DB.String)
    is_admin = DB.Column(DB.Boolean , default = False)
    email = DB.Column(DB.String)
    def __str__(self):
        return f"<User: {self.name}, id - {self.id}>"

class NewProduct(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    img = DB.Column(DB.String)
    bg = DB.Column(DB.String)
    name = DB.Column(DB.String)
    description = DB.Column(DB.String)
    price = DB.Column(DB.Integer)
    def __str__(self):
        return f"<NewProduct: {self.name}, id - {self.id}>"
