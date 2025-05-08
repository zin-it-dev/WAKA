from flask_appbuilder.charts.views import DirectByChartView, GroupByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy.sql import func
from flask_appbuilder.models.group import aggregate_count

from . import appbuilder
from .models import Genre, Book


class BookChartView(GroupByChartView):
    datamodel = SQLAInterface(Genre)
    chart_title = "Books per Genre"

    definitions = [
        {
            "label": "Books",
            "group": "name",
            "series": [
                (aggregate_count, "books"),
            ],
        }
    ]


appbuilder.add_view(
    BookChartView,
    "Book Statistics",
    icon="fa-dashboard",
    category="Statistics",
    category_icon="fa-chart-bar",
)
