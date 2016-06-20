import datetime

from flask import render_template

from ...data.models import Challenge, MarathonInfo, Prize
from ...data.db import db

def show():
    challenges = db.session.query(Challenge).all()

    # display only currently-running prizes to the user
    now = datetime.datetime.now()
    prizes = db.session.query(Prize).filter(Prize.start <= now).filter(Prize.end > now).all()

    return render_template('donate/show.tmpl', challenges=challenges, prizes=prizes)

def roi(amount):
    info = db.session.query(MarathonInfo).first()
    return str(info.roi(amount))
