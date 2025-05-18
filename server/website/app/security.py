from flask_appbuilder.security.sqla.manager import SecurityManager as FABSecurityManager

from .models import CustomUser
from .security_views import UserDBModelView


class SecurityManager(FABSecurityManager):
    user_model = CustomUser
    userdbmodelview = UserDBModelView
