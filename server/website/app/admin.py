from flask_appbuilder import IndexView


class AdminIndexView(IndexView):
    index_template = "index.html"
