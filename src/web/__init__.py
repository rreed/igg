import json
import os
import datetime

from flask import Flask, g, redirect, request, url_for, render_template, Markup
from flask.ext.login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_admin import form

from routes import register_routes
from extensions import login_manager, admin, mail
from ..data.models import Challenge, Game, Image, Interview, MarathonInfo, Prize, ScheduleEntry, User, Crew
from ..data.db import db

def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    # create a fake MarathonInfo if one doesn't exist
    # just enough to bootstrap
    info = db.session.query(MarathonInfo).first()
    if not info:
        now = datetime.datetime.now()
        half_an_hour_earlier = now - datetime.timedelta(minutes=30)
        half_an_hour_later = now + datetime.timedelta(minutes=30)

        test_game = Game.create(name='Test Game', developer='Test Dev')

        test_play = ScheduleEntry.create(
            title='Play The Test Game',
            game_id=test_game.id,
            start=half_an_hour_earlier,
            end=half_an_hour_later
        )

        MarathonInfo.create(
            start=(now - datetime.timedelta(hours=10)),
            hours=31,
            total=12345.67,
            current_game_id=test_game.id,
            next_game_id=test_game.id,
            current_schedule_entry=test_play.id
        )

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    try: # dev
        with open(os.path.join(__location__, 'secrets.json')) as secrets_file:
            secrets = json.load(secrets_file)
            app.secret_key = secrets.get('app_secret')
            app_config.SECRET_KEY = app.secret_key

            app.config.update(
                MAIL_SERVER='smtp.gmail.com',
                MAIL_PORT=465,
                MAIL_USERNAME='no-reply@iggmarathon.com',
                MAIL_DEFAULT_SENDER='no-reply@iggmarathon.com',
                MAIL_PASSWORD=secrets.get("email_password"),
                MAIL_USE_SSL=True,
                MAIL_USE_TLS=False
            )
    except IOError: # prod
        app.secret_key = os.environ.get('IGG_APP_SECRET')
        app_config.SECRET_KEY = app.secret_key

        app.config.update(
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=465,
            MAIL_USERNAME='no-reply@iggmarathon.com',
            MAIL_DEFAULT_SENDER='no-reply@iggmarathon.com',
            MAIL_PASSWORD=os.environ.get("IGG_EMAIL_PASSWORD"),
            MAIL_USE_SSL=True,
            MAIL_USE_TLS=False
        )

    login_manager.login_view = 'login.show'

    admin.add_view(AdminModelView(Challenge, db.session, endpoint='challengeadmin'))
    admin.add_view(AdminModelView(Game, db.session))
    admin.add_view(AdminModelView(MarathonInfo, db.session))
    admin.add_view(AdminModelView(Prize, db.session))
    admin.add_view(AdminModelView(Interview, db.session))
    admin.add_view(AdminModelView(ScheduleEntry, db.session))
    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Crew, db.session))
    
    admin.add_view(ImageView(Image, db.session))

    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    register_routes(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.tmpl'), 404

    @login_manager.user_loader
    def load_user(id):
        return db.session.query(User).filter_by(id=id).first()

    @app.context_processor
    def inject_marathon_info():
        marathon_info = getattr(g, "marathon_info", None)
        if not marathon_info:
            marathon_info = g.marathon_info = db.session.query(MarathonInfo).first()
        current_game = db.session.query(Game).filter_by(id=marathon_info.current_game_id).first()
        return dict(marathon_info=marathon_info, current_game=current_game)

    return app

class AdminModelView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False

    def is_accessible(self):
        if not current_user.is_anonymous:
            return current_user.is_admin()
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login.show'))

class ImageView(AdminModelView):
    def _list_thumbnail(view, context, model, name):
        if model.path:
            return Markup('<img src="%s">' % url_for('static', filename='uploaded/{}'.format(form.thumbgen_filename(model.path))))
        else:
            return ''

    column_formatters = {
        'path': _list_thumbnail
    }

    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=os.path.join(os.path.dirname(__file__), 'static/uploaded'),
                                      thumbnail_size=(100, 100, True))
    }
