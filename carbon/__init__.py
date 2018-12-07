from flask import Flask

from carbon.config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

from carbon import views
