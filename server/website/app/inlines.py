from flask_appbuilder.widgets import ListBlock
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, CompactCRUDMixin

from .models import Book


class BaseInline(CompactCRUDMixin, ModelView):
    add_exclude_columns = ["date_created"]
    edit_exclude_columns = ["date_created"]
    list_columns = ["active", "date_created"]
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
