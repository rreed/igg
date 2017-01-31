from flask import render_template

from ...data.db import db
from ...data.models import Crew 

def show():
    crew = db.session.query(Crew).filter(Crew.visible == True).order_by(Crew.order)
    return render_template('crew/show.tmpl', crew = crew)
