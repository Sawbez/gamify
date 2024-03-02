from flask import Flask

from templates.apps.views import app_blueprint

app = Flask(__name__, static_folder="./public", template_folder="./static")
app.register_blueprint(app_blueprint)
