import logging
import os

from sqlalchemy.engine.url import URL

class DevConfig(object):
    ENV = 'dev'
    HOST = 'localhost:5000'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='dev.db')
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.DEBUG

class ProdConfig(object):
    ENV = 'prod'
    HOST = 'somewhere'
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='rds somewhere probably')
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.ERROR

config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig
}

app_config = config_dict[os.getenv('ENV') or 'dev']