import logging
import os

from sqlalchemy.engine.url import URL

class BaseConfig(object):
    IGG_PARAM_RATE = 0.058
    IGG_PARAM_I_HR_COST = 10.00

    FIRST_CHARITY_EMAIL = "donate@childsplaycharity.org"
    SECOND_CHARITY_EMAIL = "info@givedirectly.org"
    THIRD_CHARITY_EMAIL = "accounting@eff.org"

class DevConfig(BaseConfig):
    ENV = 'dev'
    HOST = 'localhost:5000'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='dev.db')
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.DEBUG

class TestConfig(BaseConfig):
    ENV = 'test'
    HOST = 'localhost:5000'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='test.db')
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.DEBUG

class ProdConfig(BaseConfig):
    ENV = 'prod'
    HOST = 'dev2016.iggmarathon.com'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', URL(drivername='sqlite', database='prod.db'))
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.ERROR

config_dict = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}

app_config = config_dict[os.environ.get('ENV') or 'dev']
