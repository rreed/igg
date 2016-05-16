from flask import render_template

from ...data.db import db
from ...data.models import Game

def show():
    return render_template('index.tmpl')
