from flask import render_template, request
from flask.ext.login import current_user

from ...data.db import db
from ...data.models import MarathonInfo, ScheduleEntry, Game

def show():
    
    return render_template('overlay/show.tmpl')
