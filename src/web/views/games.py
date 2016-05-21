from flask import flash, redirect, render_template, request, url_for

from ...data.db import db
from ...data.models import Game

# GET /games
def show():
    games = db.session.query(Game).all()
    return render_template('games/show.tmpl', games=games)

# GET /games/add
def add():
    return render_template('games/add.tmpl')

# POST /games
def create():
    name = request.form.get('name')
    developer = request.form.get('developer')

    assert name
    assert developer

    Game.create(
        name=name,
        developer=developer
    )

    # TODO: flash a thing?
    return redirect(url_for('games.show'))
