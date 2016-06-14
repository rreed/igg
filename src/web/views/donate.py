from flask import render_template

from ...data.models import Challenge, MarathonInfo
from ...data.db import db

def show():
    challenges = db.session.query(Challenge).all()

    return render_template('donate/show.tmpl', challenges=challenges)

def roi(amount):
    info = db.session.query(MarathonInfo).first()
    return str(info.roi(amount))
