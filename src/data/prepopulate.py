import bcrypt
import datetime

from .models import Challenge, Game, Interview, User
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

    Challenge.create(name='Straighten the painting!', user_id=user.id, total='1000.00')
    Challenge.create(name='Tilt the painting!', user_id=user.id, total='500.00')

    Interview.create(name='Test Interview', game_id=test_game.id)
    Interview.create(name='Probably Kayin', game_id=brave_earth.id)

    print 'Prepopulated database with sample data'
