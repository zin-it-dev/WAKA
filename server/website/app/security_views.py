from flask_appbuilder.security.views import UserDBModelView as FABUserDBModelView
from flask_appbuilder.widgets import ListThumbnail
from flask_babel import lazy_gettext, gettext
from flask import request
from flask_wtf.file import FileField, FileAllowed
from werkzeug.datastructures import FileStorage
from typing import Any

from .utils import upload_image


class UserDBModelView(FABUserDBModelView):
    from .actions import muldelete, toggle_actived

    list_widget = ListThumbnail

    add_form_extra_fields = edit_form_extra_fields = {
        **FABUserDBModelView.add_form_extra_fields,
        "avatar": FileField(
            gettext("Avatar"),
            description=gettext("Avatar"),
            validators=[FileAllowed(["jpg", "png", "jpeg"], "Only images are allowed!")],
        ),
    }

    show_fieldsets = [
        (
            lazy_gettext("User info"),
            {"fields": ["username", "active", "roles", "login_count", "avatar"]},
        ),
        (
            lazy_gettext("Personal Info"),
            {"fields": ["first_name", "last_name", "email"], "expanded": True},
        ),
        (
            lazy_gettext("Audit Info"),
            {
                "fields": [
                    "last_login",
                    "fail_login_count",
                    "created_on",
                    "created_by",
                    "changed_on",
                    "changed_by",
                ],
                "expanded": False,
            },
        ),
    ]

    user_show_fieldsets = [
        (
            lazy_gettext("User info"),
            {"fields": ["username", "active", "roles", "login_count", "avatar"]},
        ),
        (
            lazy_gettext("Personal Info"),
            {"fields": ["first_name", "last_name", "email"], "expanded": True},
        ),
    ]

    label_columns = {
        "avatar_image": "Avatar",
    }

    add_columns = [
        "first_name",
        "last_name",
        "username",
        "active",
        "email",
        "roles",
        "avatar",
        "password",
        "conf_password",
    ]
    list_columns = [
        "avatar_image",
        "first_name",
        "last_name",
        "username",
        "email",
        "active",
        "roles",
    ]
    edit_columns = [
        "first_name",
        "last_name",
        "username",
        "active",
        "email",
        "roles",
        "avatar",
        "password",
        "conf_password",
    ]

    def pre_add(self, item: Any) -> None:
        file = request.files.get("avatar")
        if file and isinstance(file, FileStorage) and file.filename:
            item.avatar = upload_image(file)

        super().pre_add(item)

    def pre_update(self, item: Any) -> None:
        file = request.files.get("avatar")
        if file and isinstance(file, FileStorage) and file.filename:
            item.avatar = upload_image(file)

        super().pre_update(item)
