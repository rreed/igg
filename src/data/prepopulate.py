from .models import Game

from .db import db

def prepopulate_database():
    Game.create(
        name='Test Game',
        developer='Test Dev'
    )

    game = db.session.query(Game).first()
    assert game.name == 'Test Game'

    print 'Prepopulated database with sample data'