import flask

home = flask.Blueprint(
    name = 'home',
    import_name = 'home_app',
    template_folder = 'templates',
    static_folder='static',
    static_url_path='/home_static'
)