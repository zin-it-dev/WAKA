from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from wtforms import StringField
from flask_babel import lazy_gettext, gettext

from . import appbuilder, db
from .models import Genre, Book, Tag
from .inlines import BookInline
from .charts import BookChartView
from .widgets import CKTextAreaWidget
from .paginators import ExtraLargeResultsSetPagination


class BaseModelView(ModelView):
    from .actions import muldelete, toggle_actived, export_as_csv

    edit_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]
    add_exclude_columns = ["created_by", "created_on", "changed_by", "changed_on"]

    show_template = "appbuilder/general/model/show_cascade.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"

    list_columns = ["created_by", "created_on", "changed_by", "changed_on", "active"]
    page_size = ExtraLargeResultsSetPagination.page_size
    show_fieldsets = [
        (
            lazy_gettext("Audit Info"),
            {
                "fields": [
                    "created_on",
                    "created_by",
                    "changed_on",
                    "changed_by",
                ],
                "expanded": False,
            },
        ),
    ]


class BookModelView(BaseModelView):
    datamodel = SQLAInterface(Book)

    add_form_extra_fields = edit_form_extra_fields = {
        "description": StringField(
            gettext("Description"),
            description=gettext("Description"),
            widget=CKTextAreaWidget(),
        )
    }

    label_columns = {"image": "Image", "photo_image": "Image"}
    list_columns = [
        "photo_image",
        "title",
        "price",
        "genre",
    ] + BaseModelView.list_columns
    show_fieldsets = [
        (
            lazy_gettext("Book Info"),
            {"fields": ["photo_image", "title", "description", "price"]},
        ),
        (
            lazy_gettext("Another Info"),
            {"fields": ["tags", "genre"], "expanded": True},
        ),
    ] + BaseModelView.show_fieldsets


class GenreModelView(BaseModelView):
    datamodel = SQLAInterface(Genre)
    related_views = [BookInline, BookChartView]

    list_columns = ["name"] + BaseModelView.list_columns
    show_fieldsets = [
        (
            lazy_gettext("Genre Info"),
            {"fields": ["name"]},
        )
    ] + BaseModelView.show_fieldsets


class TagModelView(BaseModelView):
    datamodel = SQLAInterface(Tag)
    related_views = [BookModelView]
    
    list_columns = ["name"] + BaseModelView.list_columns
    show_fieldsets = [
        (
            lazy_gettext("Tag Info"),
            {"fields": ["name"]},
        )
    ] + BaseModelView.show_fieldsets


db.create_all()

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
appbuilder.add_separator("Management")
appbuilder.add_view(
    TagModelView,
    "List Tags",
    icon="fa-tag",
    category="Management",
    category_icon="fa-layer-group",
)
appbuilder.add_view_no_menu(BookInline)

appbuilder.add_link(
    "Github",
    href="https://github.com/zin-it-dev",
    icon="fa-github",
    category="Support",
    category_icon="fa-life-ring",
)
appbuilder.add_link(
    "Facebook",
    href="https://www.facebook.com/zin.it.dev",
    icon="fa-facebook",
    category="Support",
    category_icon="fa-life-ring",
)
appbuilder.add_link(
    "Instagram",
    href="https://www.instagram.com/zin.0.1.0.4",
    icon="fa-instagram",
    category="Support",
    category_icon="fa-life-ring",
)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template("404.html", base_template=appbuilder.base_template, appbuilder=appbuilder),
        404,
    )
