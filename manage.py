#!/usr/bin/env python

import sys

from flask_script import Manager, Server
from sqlalchemy.engine.url import make_url

from src.web import create_app
from src.settings import app_config
from src.data.prepopulate import prepopulate_database
from src.data.db import DatabaseConnection

app = create_app(app_config)
server = Server(host='0.0.0.0', port=5000)

manager = Manager(app)
manager.add_command("runserver", server)

@manager.command
def prepopulate():
    db_url = parse_sqlalchemy_url(app.config['SQLALCHEMY_DATABASE_URI'])
    _db = DatabaseConnection(db_url)
    with _db.transient_session():
        prepopulate_database()

def parse_sqlalchemy_url(input_url):
    try:
        url = make_url(input_url)
        _ = url.get_dialect()
        return url
    except Exception as e:
        _, e, trace = sys.exc_info()
        raise ValueError, ValueError(str(e)), trace

if __name__ == '__main__':
    manager.run()
