from app import app
from config import DEBUG
from flask_debugtoolbar import DebugToolbarExtension

if DEBUG:
    app.debug = True
    toolbar = DebugToolbarExtension(app)


app.run(host="0.0.0.0", port=8080, debug=DEBUG)
