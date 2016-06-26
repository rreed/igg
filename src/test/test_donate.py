import pytest
import time
import datetime

from flask import url_for

from src.data.models import Challenge, Donation, Game, Prize, MarathonInfo
from src.data.db import db as _db

def test_show(client):
    res = client.get(url_for('donate.show'))
    assert res.status_code == 200

def test_fails_without_amount(client):
    res = client.post(
        url_for('donate.show'),
        data=dict()
    )

    assert not res.location

def test_sub_amounts_add_to_amount_uneven(client):
    amount = 15.00

    client.post(
        url_for('donate.show'),
        data=dict(
            amount_total=amount,
            split='uneven',
            amount_first=10.00,
            amount_second=0.00,
            amount_third=5.00
        )
    )

    donation = _db.session.query(Donation).order_by(Donation.id.desc()).first()
    assert donation.amount_one == 10.00
    assert donation.amount_two == 0.00
    assert donation.amount_three == 5.00

def test_sub_amounts_add_to_amount_even(client):
    amount = 15.00

    client.post(
        url_for('donate.show'),
        data=dict(
            amount_total=amount,
            split='even'
        )
    )

    donation = _db.session.query(Donation).order_by(Donation.id.desc()).first()
    assert donation.amount_one == 5.00
    assert donation.amount_two == 5.00
    assert donation.amount_three == 5.00

def test_game_connection(client):
    now = round(time.time() * 1000)
    game = Game.create(name='Test Game {}'.format(now), developer='Test Dev')
    old_buzz = game.buzz
    amount = 15.00

    client.post(
        url_for('donate.show'),
        data=dict(
            amount_total=amount,
            game='Test Game {}'.format(now)
        )
    )

    game = _db.session.query(Game).filter_by(name='Test Game {}'.format(now)).order_by(Game.id.desc()).first()
    assert game.buzz == old_buzz + amount

def test_prize_connection(client):
    now = int(round(time.time() * 1000))
    game = Game.create(name='Test Game {}'.format(now), developer='Test Dev')

    prize = Prize.create(
        title='Another Gunbunnies Code',
        quantity=1,
        game_id=game.id,
        entry_cost=10.00,
        start=(datetime.datetime.now() - datetime.timedelta(minutes=90)),
        end=(datetime.datetime.now() + datetime.timedelta(minutes=90))
    )

    client.post(
        url_for('donate.show'),
        data=dict(
            amount_total=15.00,
            prize=prize.id
        )
    )

    donation = _db.session.query(Donation).order_by(Donation.id.desc()).first()
    assert donation.prize_id == prize.id

def test_challenge_connection(client):
    challenge = Challenge.create(name='Fake challenge', total='1000.00')
    old_total = challenge.total
    amount = 15.00

    client.post(
        url_for('donate.show'),
        data=dict(
            amount_total=amount,
            challenge=challenge.id
        )
    )

    challenge = _db.session.query(Challenge).filter_by(id=challenge.id).first()
    assert challenge.total == old_total + amount

def test_minimal_success(client):
    res = client.post(
        url_for('donate.show'),
        data=dict(amount_total=15.00)
    )

    assert 'donate' not in res.location

def test_maximal_success(client):
    res = client.post(
        url_for('donate.show'),
        data=dict(
            amount_total=15.00,
            donation_name='Not Anonymous',
            homepage='http://www.example.com',
            twitter_handle='@example',
            comment='This is a test donation blah blah blah',
            game='Test Game'
        )
    )

    assert 'donate' not in res.location

def test_total_amount_increases(client):
    info = _db.session.query(MarathonInfo).first()
    old_total = info.total
    amount = 15.00

    client.post(
        url_for('donate.show'),
        data=dict(amount_total=amount)
    )

    info = _db.session.query(MarathonInfo).first()
    assert info.total == old_total + amount
