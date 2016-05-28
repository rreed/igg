import json
import os

from flask import Flask
from flask.ext.login import LoginManager

from routes import register_routes
from ..data.models import User
from ..data.db import db

def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'secrets.json')) as secrets_file:
        secrets = json.load(secrets_file)
        app.secret_key = secrets.get('app_secret')

    register_routes(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login.show'

    @login_manager.user_loader
    def load_user(id):
        return db.session.query(User).filter_by(id=id)

    return app
