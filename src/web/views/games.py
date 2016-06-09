from flask import render_template, request, redirect, url_for
from wtforms import Form, TextField

from ...data.db import db
from ...data.models import Game

# GET /games
def show():
    games = db.session.query(Game).all()
    return render_template('games/show.tmpl', games=games)

def suggest():
    form = GameSuggestionForm(request.form)
    if request.method == 'POST':
        Game.create(name=form.name.data, developer=form.developer.data, site=form.site.data, visible=False)
        return redirect(url_for('games.suggest'))

    return render_template('games/suggest.tmpl', form=form)

class GameSuggestionForm(Form):
    name = TextField('Name')
    developer = TextField('Developer')
    site = TextField('Site')
