from flask import render_template

from ...data.db import db
from ...data.models import Game

# /games
def list():
    games = db.session.query(Game).all()
    return render_template('games.tmpl', games=games)