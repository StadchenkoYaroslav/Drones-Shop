from .urls import *
from .settings import *
from .db import *
from .loadenv import *
from .login import *

from home_app.models import *

project.register_blueprint(blueprint = home_app.home)
project.register_blueprint(blueprint = shop_app.shop_app)