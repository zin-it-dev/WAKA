from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import Genre, Book
from .utils import upload_image
from .charts import BookChartView


class GenreModelView(ModelView):
    datamodel = SQLAInterface(Genre)

    label_columns = {"is_active": "Active"}
    list_columns = ["name", "is_active"]


class BookModelView(ModelView):
    datamodel = SQLAInterface(Book)

    label_columns = {
        "image": "Photo",
        "photo_image": "Photo",
        "photo_image_thumbnail": "Photo",
    }
    list_columns = ["photo_image_thumbnail", "title", "price", "is_active"]


appbuilder.add_view(
    GenreModelView,
    "List Genres",
    icon="fa-list",
    category="Waka Management",
    category_icon="fa-layer-group",
)
appbuilder.add_view(
    BookModelView,
    "List Books",
    icon="fa-book",
    category="Waka Management",
    category_icon="fa-layer-group",
)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template("404.html", base_template=appbuilder.base_template, appbuilder=appbuilder),
        404,
    )


db.create_all()
