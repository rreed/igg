import datetime

from flask import render_template, request
from wtforms import Form, DecimalField, SelectField, TextField, TextAreaField

from ...data.models import Challenge, Donation, Game, MarathonInfo, Prize
from ...data.db import db

def show():
    challenges = db.session.query(Challenge).all()

    # display only currently-running prizes to the user
    now = datetime.datetime.now()
    prizes = db.session.query(Prize).filter(Prize.start <= now).filter(Prize.end > now).all()

    games = db.session.query(Game).all()

    challenge_tuples = [(0, 'Select a challenge...')]
    for challenge in challenges:
        if challenge.bounty:
            challenge_tuples.append((challenge.id, '{0} - (${1:.2f} / ${2:.2f})'.format(challenge.name, challenge.total, challenge.bounty)))
        else:
            challenge_tuples.append((challenge.id, '{0} - (${1:.2f})'.format(challenge.name, challenge.total)))

    prize_tuples = [(prize.id, prize.title) for prize in prizes]

    form = DonationForm(request.form)
    form.challenges.choices = challenge_tuples
    form.prizes.choices = prize_tuples

    if request.method == 'GET':
        return render_template('donate/show.tmpl', form=form, prize_count=len(prize_tuples), games=games)
    else:
        pass

def roi(amount):
    info = db.session.query(MarathonInfo).first()
    return str(info.roi(amount))

class DonationForm(Form):
    # top section
    amount_total = DecimalField('Amount')
    amount_first = DecimalField('Child\'s Play Charity')
    amount_second = DecimalField('EFF')
    amount_third = DecimalField('GiveDirectly')
    email = TextField('Email')

    # middle section
    donation_name = TextField('Name on donation')
    homepage = TextField('Homepage')
    twitter_handle = TextField('Twitter')
    comment = TextAreaField('Comment to the team')

    # selects and optional stuff
    game = TextField('Request a Game')
    challenges = SelectField('Support a Challenge')
    prizes = SelectField('Select a Prize')
