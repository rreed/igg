import json
from datetime import datetime

from flask import render_template, request
from flask.ext.login import current_user

from ...data.db import db
from ...data.models import MarathonInfo, ScheduleEntry, Game

def show():
    return render_template('schedule/show.tmpl')

def as_json():
    if request.args.get('id'):
        schedule_entries = db.session.query(ScheduleEntry)\
            .filter(ScheduleEntry.id == request.args.get('id'))
    else:
        start = request.args.get('start')
        end = request.args.get('end')
        schedule_entries = db.session.query(ScheduleEntry)\
            .filter(ScheduleEntry.start >= start)\
            .filter(ScheduleEntry.end <= end)\
            .filter(ScheduleEntry.visible == True)

    ret = []
    for entry in schedule_entries:
        if entry.prize_id:
            entry_type = 'prize'
        elif entry.interview_id:
            entry_type = 'interview'
        else:
            entry_type = 'game'
        
        highlighted = None
        #highlight commented items in schedule
        if entry.opscomment and \
            not current_user.is_anonymous and\
            current_user.is_admin():
            highlighted = "red"

        ret.append({
            "id": entry.id,
            "eventId": entry.id,
            "title": entry.title if entry.title else entry.game.name,
            "start": entry.start.isoformat(),
            "end": entry.end.isoformat(),
            "resourceId": entry_type,
            "gameId": entry.game.id,
            "opscomment": entry.opscomment,
            "color": highlighted,
        })
        
    return json.dumps(ret)

def ajax_create():
    #this isn't convoluted
    if not current_user.is_anonymous and current_user.is_admin():
        action = request.form.get('action')
        pk = request.form.get('pk')
        try:
            if action == 'delete':
                if pk <= 0:#laaaaazy
                    return 'new/empty event, no server action'
                entry = db.session.query(ScheduleEntry).get(pk)
                db.session.delete(entry)
                db.session.commit()
                return 'deleted ' + pk
            elif action == 'new':
                data = json.loads(request.form.get('info'))
                entry = ScheduleEntry()
                entry.title =       data['name']
                entry.game =        db.session.query(Game).get(data['game'])
                entry.opscomment =  data['opscomment']
                entry.start =   datetime.strptime(data['start'], '%Y-%m-%d %H:%M:%S')
                entry.end =     datetime.strptime(data['end'], '%Y-%m-%d %H:%M:%S')
                entry.visible = True
                db.session.add(entry)
                db.session.commit()

                return 'new entry ' + unicode(entry.id)
            elif action == 'edit':
                entry = db.session.query(ScheduleEntry).get(pk)
                data = json.loads(request.form.get('info'))
                entry.title =       data['name']
                entry.game =        db.session.query(Game).get(data['game'])
                entry.opscomment =  data['opscomment']
                entry.start =   datetime.strptime(data['start'], '%Y-%m-%d %H:%M:%S')
                entry.end =     datetime.strptime(data['end'], '%Y-%m-%d %H:%M:%S')

                db.session.commit()
                return 'edited ' + pk
            else:
                return 'but nothing happened'
        except Exception as e:
            print e
            return unicode(e)
        return 'success?'
    return 'no auth' 


def elapsed():
    info = db.session.query(MarathonInfo).first()
    return info.elapsed()
