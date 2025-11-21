import flask, os, flask_login
from .models import *
import math

def check_admin() -> bool:
    if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
        return True
    return False

COUNT_PRODUCT_PAGE = 3

def render_catalog():
    page = int(flask.request.args.get("page", 1))
    is_admin = check_admin()
    if flask.request.method == "POST" and is_admin:
        # for i in range(40):
        new_product = Product(
            name = flask.request.form.get("name"),
            price = flask.request.form.get("price"),
            description = flask.request.form.get("description"),
            count = flask.request.form.get("count"),
            discount = flask.request.form.get("discount"),
        )
        
        DB.session.add(new_product)
        DB.session.commit()
        image = flask.request.files.get('image')
        image.save(
            dst = os.path.abspath(os.path.join(__file__, '..', 'static', 'images', "products", f'{new_product.id}.png'))
        )
    all_products = Product.query.paginate(
        page = page,
        per_page = COUNT_PRODUCT_PAGE
    )
    last_page = math.ceil(all_products.total / COUNT_PRODUCT_PAGE)
    # math.ceil - округляет в большую сторону
    return flask.render_template("catalog.html", admin = is_admin, products = all_products, page = page, last_page = last_page)

def delete(id: int):
    if check_admin():
        product = Product.query.get(id)
        if product:
            DB.session.delete(product)
            DB.session.commit()
            image_path = os.path.abspath(os.path.join(__file__, '..', 'static', 'images', "products", f'{id}.png'))
            os.remove(image_path)
    return flask.redirect('/catalog')

def render_change(id: int):
    if check_admin():
        product = Product.query.get(id)
        # Модель.query.get(id) - отримує запис з моделі (БД) за id
        if flask.request.method == "POST":
            product.name = flask.request.form.get("name")
            product.price = flask.request.form.get("price")
            product.count = flask.request.form.get("count")
            product.discount = flask.request.form.get("discount")
            product.description = flask.request.form.get("description")
            DB.session.commit()
            image = flask.request.files.get('image')
            if image:
                image.save(
                    dst = os.path.abspath(os.path.join(__file__, '..', 'static', 'images', "products", f'{product.id}.png'))
                )
            return flask.redirect('/catalog')
        return flask.render_template("change.html", product = product)
        
def buy(id: int):
    product = Product.query.get(id)
    response = flask.make_response(flask.redirect('/catalog'))
    # flask.make_response - функція яка створює відповідь користувачу ( для змінення його cookie ). 
    # В дужках потрібно redirect або render_template
    
    # flask.request.cookies.get('назва') - отримує cookie
    # response.set_cookie('назва', 'значення') - вказує cookie
    if product:
        products = flask.request.cookies.get('list_products')
        if products:
            response.set_cookie('list_products', products + "|" + str(id))
        else:
            response.set_cookie('list_products', str(id))
    return response