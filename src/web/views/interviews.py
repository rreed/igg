from flask import render_template

from ...data.db import db
from ...data.models import Interview

def show():
    interviews = db.session.query(Interview).all()
    return render_template('interviews/show.tmpl', interviews=interviews)
