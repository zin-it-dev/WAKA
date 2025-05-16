import csv, io

from flask import redirect, flash, make_response
from flask_babel import gettext
from flask_appbuilder.actions import action


@action("muldelete", "Delete", "Delete all Really?", "fa-rocket", single=False)
def muldelete(self, items):
    self.datamodel.delete_all(items)
    flash(gettext("Deleted %(count)s items successfully", count=len(items)), category="success")
    self.update_redirect()
    return redirect(self.get_redirect())


@action("mulactivate", "Activate", "Toggle active state all Really?", "fa-check", single=False)
def toggle_actived(self, items):
    for item in items:
        item.active = not item.active
        self.datamodel.edit(item)

    flash(gettext("Toggled active state for %(count)s items", count=len(items)), category="success")
    self.update_redirect()
    return redirect(self.get_redirect())


@action(
    "export_csv", "Export as CSV", "Export selected records as CSV?", "fa-download", single=False
)
def export_as_csv(self, items):
    meta = self.datamodel.obj.__tablename__
    field_names = self.datamodel.get_columns_list()

    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)

    writer.writerow(field_names)
    for obj in items:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    csv_content = csv_buffer.getvalue()
    csv_buffer.close()

    response = make_response(csv_content)
    response.headers["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
    response.headers["Content-Type"] = "text/csv"
    return response
