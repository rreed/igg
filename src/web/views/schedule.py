import json

from flask import render_template, request

from ...data.db import db
from ...data.models import ScheduleEntry

def show():
    return render_template('schedule/show.tmpl')

def as_json():
    start = request.args.get('start')
    end = request.args.get('end')
    schedule_entries = db.session.query(ScheduleEntry)\
        .filter(ScheduleEntry.start >= start)\
        .filter(ScheduleEntry.end <= end)\
        .all()

    ret = []
    for entry in schedule_entries:
        if entry.prize_id:
            entry_type = 'prize'
        elif entry.interview_id:
            entry_type = 'interview'
        else:
            entry_type = 'game'

        ret.append({
            "id": entry.id,
            "title": entry.title,
            "start": entry.start.isoformat(),
            "end": entry.end.isoformat(),
            "resourceId": entry_type
        })

    return json.dumps(ret)
