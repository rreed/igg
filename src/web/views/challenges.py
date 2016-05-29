from flask import render_template

from ...data.db import db
from ...data.models import Challenge

def show():
    challenges = db.session.query(Challenge).all()
    return render_template('challenges/show.tmpl', challenges=challenges)
