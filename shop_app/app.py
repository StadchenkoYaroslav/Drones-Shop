import flask

shop_app = flask.Blueprint(
    name='shop_app',
    import_name='shop_app',
    template_folder='templates',
    static_folder='static',
    static_url_path='/shop_app_static'
)