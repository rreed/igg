from flask import render_template

from ...data.db import db
from ...data.models import Image, Prize

def list():
    prizes = db.session.query(Prize).all()
    return render_template('prizes/list.tmpl', prizes=prizes)

def show(prize_id):
    prize = db.session.query(Prize).filter_by(id=prize_id).first()
    images = db.session.query(Image).filter_by(prize_id=prize_id).all()
    return render_template('prizes/show.tmpl', prize=prize, images=images)
