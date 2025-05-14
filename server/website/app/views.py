from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

from . import appbuilder, db
from .models import Genre, Book, Tag


class BaseModelView(ModelView):
    list_columns = ["is_active", "date_created", "date_updated"]


class BookModelView(BaseModelView):
    datamodel = SQLAInterface(Book)

    label_columns = {
        "image": "Photo",
        "photo_image": "Photo",
        "photo_image_thumbnail": "Photo",
    }
    list_columns = [
        "photo_image_thumbnail",
        "title",
        "price",
        "genre",
    ] + BaseModelView.list_columns


class GenreModelView(BaseModelView):
    datamodel = SQLAInterface(Genre)
    list_columns = ["name"] + BaseModelView.list_columns
    related_views = [BookModelView]


class TagModelView(BaseModelView):
    datamodel = SQLAInterface(Tag)
    list_columns = ["name"] + BaseModelView.list_columns
    related_views = [BookModelView]


appbuilder.add_view(
    GenreModelView,
    "List Genres",
    icon="fa-list",
    category="Management",
    category_icon="fa-layer-group",
)
appbuilder.add_view(
    BookModelView,
    "List Books",
    icon="fa-book",
    category="Management",
    category_icon="fa-layer-group",
)
appbuilder.add_view(
    TagModelView,
    "List Tags",
    icon="fa-tag",
    category="Management",
    category_icon="fa-layer-group",
)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template("404.html", base_template=appbuilder.base_template, appbuilder=appbuilder),
        404,
    )


db.create_all()
