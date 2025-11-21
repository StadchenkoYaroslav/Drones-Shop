import flask, flask_login
from .models import *
from project.db import *

def render_home():
    if flask_login.current_user.is_authenticated:
        print(flask_login.current_user)
    
    return flask.render_template("home.html")

def render_registation():
    if flask.request.method == 'POST':
        user_new = User(
            name = flask.request.form.get('name'),
            password = flask.request.form.get('password')
        )
        DATABASE.session.add(user_new)
        DATABASE.session.commit()
        image = flask.request.files.get("image")
        # flask.request.files.get("ключ") - отримує файл з форми
        # file.save(path) - зберігає отриманий файл за шляхом
        image.save(
            dst = os.path.abspath(os.path.join(__file__, "..", "static", "images", "profiles", f"{user_new.name}.png "))
        )
        
        return flask.redirect("/login")
    return flask.render_template('reg.html')

def render_login():
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
        
    return flask.render_template("login.html")

def logout():
    flask_login.logout_user()
    return flask.redirect("/")

def render_listusers():
    users = User.query.all()

    return flask.render_template('users.html', users = users)