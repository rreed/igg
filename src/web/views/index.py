from flask import render_template

from ...data.db import db
from ...data.models import Game

def index():
    games = db.session.query(Game).all()
    return render_template('index.tmpl', games=games)