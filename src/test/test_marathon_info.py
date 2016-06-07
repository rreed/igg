import datetime

from src.data.models import MarathonInfo, Game, ScheduleEntry
from src.data.db import db as _db

def setup_module(cls):
    cls.now = datetime.datetime.now()
    cls.test_game = _db.session.query(Game).first()
    cls.test_play = _db.session.query(ScheduleEntry).first()

def test_stage_pre():
    info = MarathonInfo.create(
        start=(now + datetime.timedelta(hours=1)),
        hours=20,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id,
        total=12345.67
    )
    assert info.stage() == 'PRE'

def test_stage_live():
    info = MarathonInfo.create(
        start=(now - datetime.timedelta(hours=10)),
        hours=20,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id,
        total=12345.67
    )
    assert info.stage() == 'LIVE'

def test_stage_post():
    info = MarathonInfo.create(
        start=(now - datetime.timedelta(hours=30)),
        hours=20,
        current_game_id=test_game.id,
        next_game_id=test_game.id,
        current_schedule_entry=test_play.id,
        total=12345.67
    )
    assert info.stage() == 'POST'
