import os, cloudinary

from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

DEBUG_TB_INTERCEPT_REDIRECTS = False

SECRET_KEY = "g%qqd5v6+d)^2h7pt7l1p50+aqw#oy0oax%0f5w!x^xzn%*sc8"

DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER = os.getenv("DB_SERVER")

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "database", DB_NAME)
# SQLALCHEMY_DATABASE_URI = (
#     f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?charset=utf8mb4"
# )

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = "WAKA 🔖"

# Uncomment to setup Setup an App icon
# APP_ICON = "static/img/logo.jpg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = "Admin"

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = "Public"

# Will allow user self registration
AUTH_USER_REGISTRATION = False

# ---------------------------------------------------
# Babel config for translations
# ---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = "en"
# Your application default translation path
BABEL_DEFAULT_FOLDER = "translations"
# The allowed translation for you app
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Pt Brazil"},
    "es": {"flag": "es", "name": "Spanish"},
    "de": {"flag": "de", "name": "German"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "pl": {"flag": "pl", "name": "Polish"},
}

# Theme configuration
# these are located on static/appbuilder/css/themes
APP_THEME = "slate.css"

# Swagger
FAB_API_SWAGGER_UI = True

# Customize
FAB_SECURITY_MANAGER_CLASS = "app.security.SecurityManager"

# Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET"),
)
