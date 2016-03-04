from flask import redirect, render_template, request, url_for

from ...data.db import db
from ...data.models import Game

# GET /games
def list():
    games = db.session.query(Game).all()
    return render_template('games/list.tmpl', games=games)

# GET /games/add
def add():
    return render_template('games/add.tmpl')

# POST /games
def create():
    name = request.form.get('name')
    developer = request.form.get('developer')

    assert name is not None
    assert developer is not None

    Game.create(
        name=name,
        developer=developer
    )

    # TODO: flash a thing?
    return redirect(url_for('games.list'))