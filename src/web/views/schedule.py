from flask import render_template

from ...data.db import db
from ...data.models import ScheduleEntry

def show():
    schedule_entries = db.session.query(ScheduleEntry).all()
    return render_template('schedule/show.tmpl', schedule_entries=schedule_entries)
