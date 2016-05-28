import json
import os

from flask import Flask
from flask.ext.login import LoginManager
from flask_bcrypt import Bcrypt

from routes import register_routes

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

    bcrypt = Bcrypt(app)

    @login_manager.user_loader
    def load_user(id):
        return User.get(int(id))

    return app
