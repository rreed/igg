import pytest

from flask import url_for
from wtforms import ValidationError

from src.data.models import User
from src.data.db import db as _db

def setup_module(cls):
    # has to be here or teardown_module won't get called
    pass

def teardown_module(cls):
    _db.session.query(User).filter_by(username='register').delete()
    _db.session.commit()

def test_show(client):
    res = client.get(url_for('register.show'))
    assert res.status_code == 200

def test_register_fails_no_email(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', email='example@example.com', confirm='password')
    )

    assert res.location is None

def test_register_fails_no_password(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', email='test@example.com', confirm='password')
    )

    assert res.location is None

def test_register_fails_no_username(client):
    res = client.post(
        url_for('register.show'),
        data=dict(password='password', email='test@example.com', confirm='password')
    )

    assert res.location is None

def test_register_fails_username_too_short(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='u', password='password', email='test@example.com', confirm='password')
    )

    assert res.location is None


def test_register_fails_username_too_long(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='usernameusernameusernameusernameusername', password='password', email='test@example.com', confirm='password')
    )

    assert res.location is None

def test_register_fails_password_too_short(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', password='p', email='test@example.com', confirm='p')
    )

    assert res.location is None

def test_register_fails_password_too_long(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', password='passwordpasswordpasswordpasswordpasswordpasswordpassword', email='test@example.com', confirm='passwordpasswordpasswordpasswordpasswordpasswordpassword')
    )

    assert res.location is None

def test_register_fails_email_too_short(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', password='password', email='t', confirm='password')
    )

    assert res.location is None

def test_register_fails_email_too_long(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', password='password', email='wowthisisareallylongemailaddresswhowouldevergiveussomethinglikethis@example.com', confirm='password')
    )

    assert res.location is None

def test_register_fails_mismatched_passwords(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='username', password='password1', email='example@example.com', confirm='password2')
    )

    assert res.location is None

def test_register_succeeds(client):
    res = client.post(
        url_for('register.show'),
        data=dict(username='register', password='password', email='register@example.com', confirm='password')
    )

    assert res.status_code == 302
