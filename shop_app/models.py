from project.db import DATABASE as DB

class Product(DB.Model):
    id = DB.Column(DB.Integer , primary_key=True)
    name = DB.Column(DB.String(255), unique=True)
    price = DB.Column(DB.Float)
    description = DB.Column(DB.String)
    count = DB.Column(DB.Integer)
    discount = DB.Column(DB.Integer)

    def __str__(self):
        return f'<Product {self.name}, id - {self.id}, price - {self.price}> '
    def get_path(self):
        return f'images/products/{self.id}.png'