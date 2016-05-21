import pytest

from src.web import create_app
from src.settings import app_config
from src.data.db import DatabaseConnection
from src.data.prepopulate import prepopulate_database

from flask.ext.sqlalchemy import SQLAlchemy

@pytest.fixture
def app():
    app = create_app(app_config)
    return app

@pytest.fixture
def db(scope='session'):
    app = create_app(app_config)
    _db = SQLAlchemy(app)
    _db.create_all()
    return _db
