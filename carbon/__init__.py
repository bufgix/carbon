from flask import Flask
from flask_cors import CORS, cross_origin

from carbon.config import Config


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(Config)
app.url_map.strict_slashes = False

from carbon import views
