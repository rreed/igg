import bcrypt
import datetime

from .models import Challenge, Game, Interview, MarathonInfo, Prize, ScheduleEntry, User
from .db import db
from ..settings import app_config

def prepopulate_database():
    # bail to make sure this never runs in prod
    if app_config.ENV is not 'dev':
        print 'Please do not run this in production~'
        return

    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw('password'.encode('utf-8'), salt)
    user = User.create(
        username='blogspot',
        password=hashed_pw,
        salt=salt,
        email='example@example.com',
        created_at=datetime.datetime.utcnow()
    )

    test_game = Game.create(name='Test Game', developer='Test Dev')
    brave_earth = Game.create(name='Brave Earth: Epilogue', developer='Not Kayin')

    Challenge.create(name='Straighten the painting!', total='1000.00')
    Challenge.create(name='Tilt the painting!', total='500.00')

    Interview.create(name='Test Interview', game_id=test_game.id)
    kayin = Interview.create(name='Probably Kayin', game_id=brave_earth.id)

    now = datetime.datetime.now()
    half_an_hour_earlier = now - datetime.timedelta(minutes=30)
    half_an_hour_later = now + datetime.timedelta(minutes=30)

    test_play = ScheduleEntry.create(
        title='Play The Test Game',
        game_id=test_game.id,
        start=half_an_hour_earlier,
        end=half_an_hour_later
    )

    ScheduleEntry.create(
        title='Yell at Kayin',
        game_id=brave_earth.id,
        interview_id=kayin.id,
        start=(now - datetime.timedelta(minutes=90)),
        end=(now - datetime.timedelta(minutes=30))
    )

    prize = Prize.create(
        title='Another Gunbunnies Code',
        quantity=1,
        game_id=test_game.id,
        entry_cost=10.00,
        start=(now - datetime.timedelta(minutes=90)),
        end=(now + datetime.timedelta(minutes=90))
    )
    Prize.create(
        title='Some Cool Test Swag',
        quantity=3,
        game_id=test_game.id,
        entry_cost=5.00,
        start=(now - datetime.timedelta(minutes=120)),
        end=(now + datetime.timedelta(minutes=120))
    )

    ScheduleEntry.create(
        title='Win a code',
        game_id=test_game.id,
        prize_id=prize.id,
        start=(now + datetime.timedelta(minutes=30)),
        end=(now + datetime.timedelta(minutes=90))
    )

    # change this to test things, but basically just assume we're in the middle of things
    MarathonInfo.create(
        start=(now - datetime.timedelta(hours=10)),
        hours=31,
        total=12345.67,
        current_game_id=test_game.id,
        next_game_id=brave_earth.id,
        current_schedule_entry=test_play.id
    )

    print 'Prepopulated database with sample data'
