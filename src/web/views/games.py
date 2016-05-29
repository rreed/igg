from flask import render_template

from ...data.db import db
from ...data.models import Game

# GET /games
def show():
    games = db.session.query(Game).all()
    return render_template('games/show.tmpl', games=games)
