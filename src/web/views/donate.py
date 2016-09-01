import datetime
import random
import string

from flask import render_template, request, redirect, url_for
from wtforms import Form, DecimalField, RadioField, SelectField, TextField, TextAreaField, validators
from flask.ext.login import current_user

from ...data.models import Challenge, Donation, Game, MarathonInfo, Prize
from ...data.db import db
from ...web.extensions import paypal
from ...settings import app_config

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

    prize_tuples = [(0, 'Select a prize...')]
    for prize in prizes:
        prize_tuples.append((prize.id, prize.title))

    form = DonationForm(request.form)
    form.challenge.choices = challenge_tuples
    form.prize.choices = prize_tuples

    if request.method == 'POST' and form.validate():
        # oh boy validation
        # snag all the absolutely required things first
        amount = form.amount_total.data

        # better names when we finalize charities
        if form.split.data == 'even':
            split = round(amount / 3, 2) # two-digit precision
            delta = round((split * 3) - float(amount), 2)
            one = split
            two = split
            three = split - delta
        else:
            one = form.amount_first.data
            two = form.amount_second.data
            three = form.amount_third.data

        email = form.email.data
        name = form.donation_name.data or 'Anonymous'
        homepage = form.homepage.data
        twitter = form.twitter_handle.data
        comment = form.comment.data

        game_name = form.game.data
        game = db.session.query(Game).filter_by(name=game_name).first()
        game_id = game.id if game else None

        challenge = form.challenge.data
        challenge_id = challenge if challenge != 0 else None

        prize = form.prize.data
        prize_id = prize if prize != 0 else None

        user_id = current_user.id if not current_user.is_anonymous else None

        populate_paypal_info(one, two, three)

        Donation.create(
            name=name,
            url=homepage,
            twitter=twitter,
            comment=comment,
            amount=amount,
            amount_one=one,
            amount_two=two,
            amount_three=three,
            time=datetime.datetime.now(),
            user_id=user_id,
            prize_id=prize_id,
            challenge_id=challenge_id,
            game_id=game_id
        )

        # add this donation to the total number of donations
        info = db.session.query(MarathonInfo).first()
        info.total += float(amount)
        info.update()

        # if we know about their game, add some buzz
        if game:
            game.buzz += float(amount)
            game.update()

        # if a challenge was selected, update it
        if challenge_id:
            challenge = db.session.query(Challenge).filter_by(id=challenge_id).first()
            challenge.total += float(amount)
            challenge.update()

        return redirect(url_for('index.show'))

    # GET
    return render_template('donate/show.tmpl', form=form, prize_count=len(prize_tuples), games=games)

def thanks():
    return render_template('donate/thanks.tmpl')

def roi(amount):
    info = db.session.query(MarathonInfo).first()
    return str(info.roi(amount))

def populate_paypal_info(first, second, third):
    if app_config.ENV == 'test':  # don't spam Paypal with unit tests
        return ""

    sender_batch_id = ''.join(random.choice(string.ascii_uppercase) for i in range(12))

    items = []
    if first > 0:
        items.append(create_donation_recipent(first, app_config.FIRST_CHARITY_EMAIL))

    if second > 0:
        items.append(create_donation_recipent(second, app_config.SECOND_CHARITY_EMAIL))

    if third > 0:
        items.append(create_donation_recipent(third, app_config.THIRD_CHARITY_EMAIL))

    payout = paypal.Payout({
        "sender_batch_header": {
            "sender_batch_id": sender_batch_id
        },
        "items": items
    })

    if payout.create():
        return payout
    else:
        raise Exception(payout.error)

def create_donation_recipent(amount, email):
    return {
        "recipient_type": "EMAIL",
        "amount": {
            "value": amount,
            "currency": "USD"
        },
        "receiver": email
    }

class DonationForm(Form):
    # top section
    amount_total = DecimalField('Amount', [validators.DataRequired()])
    split = RadioField('Split Donation', choices=[('even','Evenly'), ('uneven','Custom')], default='even')
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
    challenge = SelectField('Support a Challenge', coerce=int, default=0)
    prize = SelectField('Select a Prize', coerce=int, default=0)
