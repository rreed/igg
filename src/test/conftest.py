import pytest

from src.web import create_app
from src.settings import app_config

@pytest.fixture
def app():
    app = create_app(app_config)
    return app
