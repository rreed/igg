from flask import Flask

from routes import register_routes

def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    register_routes(app)

    return app