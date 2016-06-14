from flask import render_template

from ...data.models import MarathonInfo
from ...data.db import db

def show():
    return render_template('donate/show.tmpl')

def roi(amount):
    info = db.session.query(MarathonInfo).first()
    return str(info.roi(amount))
