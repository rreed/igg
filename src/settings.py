import logging
import os

from sqlalchemy.engine.url import URL

IGG_PARAM_RATE = 0.058
IGG_PARAM_I_HR_COST = 10.00

class DevConfig(object):
    ENV = 'dev'
    HOST = 'localhost:5000'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='dev.db')
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.DEBUG

    IGG_PARAM_RATE = IGG_PARAM_RATE
    IGG_PARAM_I_HR_COST = IGG_PARAM_I_HR_COST

class TestConfig(object):
    ENV = 'test'
    HOST = 'localhost:5000'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = URL(drivername='sqlite', database='test.db')
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.DEBUG

    IGG_PARAM_RATE = IGG_PARAM_RATE
    IGG_PARAM_I_HR_COST = IGG_PARAM_I_HR_COST


class ProdConfig(object):
    ENV = 'prod'
    HOST = 'dev2016.iggmarathon.com'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', URL(drivername='sqlite', database='prod.db'))
    SQLALCHEMY_SESSION_ARGS = {}

    APP_LOG_LEVEL = logging.ERROR

    IGG_PARAM_RATE = IGG_PARAM_RATE
    IGG_PARAM_I_HR_COST = IGG_PARAM_I_HR_COST

config_dict = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}

app_config = config_dict[os.environ.get('ENV') or 'dev']
