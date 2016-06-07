import pytest
import datetime

from src.web import create_app
from src.settings import app_config
from src.data.db import DatabaseConnection
from src.data.models import Game, ScheduleEntry, MarathonInfo

from flask.ext.sqlalchemy import SQLAlchemy

@pytest.fixture
def app():
    app = create_app(app_config)
    return app

@pytest.fixture(scope='session', autouse=True)
def marathon_info_fixture():
    print 'CREATING STUFF'
    now = datetime.datetime.now()
    test_game = Game.create(name='Test Game', developer='Test Dev')

    test_play = ScheduleEntry.create(
        title='Play The Test Game',
        game_id=test_game.id,
        start=(now - datetime.timedelta(minutes=30)),
        end=(now + datetime.timedelta(minutes=30))
    )
    MarathonInfo.create(
        start=(now - datetime.timedelta(hours=10)),
        hours=31,
        total=12345.67,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id
    )
