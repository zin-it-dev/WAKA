from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from wtforms import StringField
from flask_babel import gettext

from . import appbuilder, db
from .models import Genre, Book, Tag
from .inlines import BookInline
from .charts import BookChartView
from .widgets import CKTextAreaWidget
from .paginators import ExtraLargeResultsSetPagination


class BaseModelView(ModelView):
    from .actions import muldelete, toggle_actived, export_as_csv

    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"

    add_exclude_columns = edit_exclude_columns = ["date_created"]
    list_columns = ["active", "date_created"]
    page_size = ExtraLargeResultsSetPagination.page_size


class BookModelView(BaseModelView):
    datamodel = SQLAInterface(Book)

    add_form_extra_fields = edit_form_extra_fields = {
        "description": StringField(
            gettext("Description"),
            description=gettext("Description"),
            widget=CKTextAreaWidget(),
        )
    }

    label_columns = {"image": "Image", "photo_image": "Image", "photo_image_thumbnail": "Image"}
    list_columns = [
        "photo_image_thumbnail",
        "title",
        "price",
        "genre",
    ] + BaseModelView.list_columns
    show_columns = [
        "photo_image",
        "title",
        "price",
        "active",
        "description",
        "type",
        "quantity",
        "tags",
        "genre",
        "date_created",
    ]


class GenreModelView(BaseModelView):
    datamodel = SQLAInterface(Genre)
    related_views = [BookInline, BookChartView]

    list_columns = ["name"] + BaseModelView.list_columns


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
appbuilder.add_view_no_menu(BookInline)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template("404.html", base_template=appbuilder.base_template, appbuilder=appbuilder),
        404,
    )


db.create_all()
