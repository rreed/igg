import datetime

from src.data.models import MarathonInfo, Game, ScheduleEntry
from src.data.db import db as _db

def setup_module(cls):
    cls.now = datetime.datetime.now()
    cls.test_game = Game.create(name='Test Game', developer='Test Dev')
    cls.test_play = ScheduleEntry.create(
        title='Play The Test Game',
        game_id=test_game.id,
        start=(now - datetime.timedelta(minutes=30)),
        end=(now + datetime.timedelta(minutes=30))
    )

def teardown_module(cls):
    _db.session.query(Game).filter_by(name='Test Game').delete()
    _db.session.commit()

def test_stage_pre():
    info = MarathonInfo.create(
        start=(now + datetime.timedelta(hours=1)),
        hours=20,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id
    )
    assert info.stage() == 'PRE'

def test_stage_live():
    info = MarathonInfo.create(
        start=(now - datetime.timedelta(hours=10)),
        hours=20,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id
    )
    assert info.stage() == 'LIVE'

def test_stage_post():
    info = MarathonInfo.create(
        start=(now - datetime.timedelta(hours=30)),
        hours=20,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id
    )
    assert info.stage() == 'POST'
