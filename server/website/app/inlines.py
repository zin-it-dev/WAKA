from flask_appbuilder.widgets import ListBlock
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, CompactCRUDMixin

from .models import Book


class BaseInline(CompactCRUDMixin, ModelView):
    add_exclude_columns = edit_exclude_columns = ["created_on", "changed_on"]
    list_columns = ["active"]
    list_widget = ListBlock


class BookInline(BaseInline):
    datamodel = SQLAInterface(Book)

    label_columns = {
        "image": "Photo",
        "photo_image": "Photo",
    }
    list_columns = [
        "photo_image",
        "title",
        "price",
        "description",
    ] + BaseInline.list_columns
