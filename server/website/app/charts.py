from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.group import aggregate_count

from . import appbuilder
from .models import Book


class BookChartView(GroupByChartView):
    datamodel = SQLAInterface(Book)
    chart_title = "Book Statistics"

    definitions = [
        {
            "label": "Book Count By Genres",
            "group": "genre.name",
            "series": [
                (aggregate_count, "title"),
            ],
        }
    ]


appbuilder.add_view(
    BookChartView,
    "Book's Statistics",
    icon="fa-dashboard",
    category="Statistics",
    category_icon="fa-chart-bar",
)
