from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelRestApi

from . import appbuilder
from .models import Genre, Book
from .paginators import (
    LargeResultsSetPagination,
    ExtraLargeResultsSetPagination,
    StandardResultsSetPagination,
)


class BaseRestApi(ModelRestApi):
    allow_browser_login = True
    list_columns = ["id", "active"]
    page_size = StandardResultsSetPagination.page_size


class GenreRestApi(BaseRestApi):
    resource_name = "genres"
    datamodel = SQLAInterface(Genre)
    list_columns = BaseRestApi.list_columns + ["name"]

    exclude_route_methods = ["get", "put", "post", "delete", "info"]
    openapi_spec_methods = {
        "get_list": {
            "get": {
                "description": "Get all genres",
            }
        }
    }


class BookRestApi(BaseRestApi):
    resource_name = "books"
    datamodel = SQLAInterface(Book)
    list_columns = BaseRestApi.list_columns + [
        "title",
        "price",
        "image",
        "quantity",
        "genre.name",
        "tags.name",
    ]
    page_size = LargeResultsSetPagination.page_size


appbuilder.add_api(GenreRestApi)
appbuilder.add_api(BookRestApi)
