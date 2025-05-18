import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_appbuilder.menu import Menu
from flask_cors import CORS

from .security import SecurityManager
from .admin import AdminIndexView

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)


app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(
    app,
    db.session,
    menu=Menu(reverse=False),
    security_manager_class=SecurityManager,
    indexview=AdminIndexView,
)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

from . import views, models, apis, charts
