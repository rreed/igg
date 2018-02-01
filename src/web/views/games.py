import json

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

#machine digestible list of games
def as_json():
    if request.args.get('id'):
        games_entries = db.session.query(Game).filter(Game.id == request.args.get('id'))
    else:
        games_entries = db.session.query(Game).filter(Game.visible)

    ret = []
    for game in games_entries:
        ret.append({
            'name': game.name,
            'dev': game.developer,
            'site': game.site,
            'buzz': game.buzz,
            'pk': game.id,
        })

    return json.dumps(ret)

class GameSuggestionForm(Form):
    name = TextField('Name')
    developer = TextField('Developer')
    site = TextField('Site')
