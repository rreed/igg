import bcrypt
import datetime

from .models import Challenge, Game, User
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

    Challenge.create(name='Straighten the painting!', user_id=user.id, total='1000.00')
    Challenge.create(name='Tilt the painting!', user_id=user.id, total='500.00')

    print 'Prepopulated database with sample data'
