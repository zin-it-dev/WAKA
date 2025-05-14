from flask_appbuilder.security.sqla.manager import SecurityManager as FABSecurityManager

from .models import User
from .security_views import UserDBModelView


class SecurityManager(FABSecurityManager):
    user_model = User
    userdbmodelview = UserDBModelView
