import flask, flask_login
from .models import *
from project.db import *
from shop_app.models import *
from shop_app.views import count_cart_product

def render_home():
    new_products = NewProduct.query.all()
    list_products = Product.query.limit(4)
    return flask.render_template("home.html", new_products=new_products, products = list_products, count_cart = count_cart_product())
    
def render_registation():
    if not flask_login.current_user.is_authenticated:
        if flask.request.method == 'POST':
            if flask.request.form.get("password") == flask.request.form.get("confirm-password"):
                user_new = User(
                    name = flask.request.form.get('name'),
                    password = flask.request.form.get('password'),
                    email  = flask.request.form.get("email")
                )
                DATABASE.session.add(user_new)
                DATABASE.session.commit()
    
                return flask.redirect("/login")
        return flask.render_template('reg.html', count_cart = count_cart_product())
    else:
        return flask.redirect("/")

def render_login():
    if not flask_login.current_user.is_authenticated:
        if flask.request.method == 'POST':
            user = User.query.filter_by(
                name = flask.request.form.get('name'),
                password = flask.request.form.get('password')   
            ).first()
            if user:
                flask_login.login_user(user)
                return flask.redirect("/")
                
            else:
                print('User does not exist')
            
        return flask.render_template("login.html", count_cart = count_cart_product())
    else:
        return flask.redirect("/")
def logout():
    flask_login.logout_user()
    return flask.redirect("/")