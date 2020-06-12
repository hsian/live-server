from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name):
    app = Flask(__name__, static_folder='../client')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app