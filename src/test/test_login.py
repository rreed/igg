import pytest
import bcrypt

from flask import url_for

from src.data.models import User
from src.data.db import db as _db

def setup_module(cls):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw('password', salt)
    user = User.create(username='username', password=hashed_pw, email='username@example.com', salt=salt)

def teardown_module(cls):
    _db.session.query(User).filter_by(username='username').delete()
    _db.session.commit()

def test_show(client):
    res = client.get(url_for('login.show'))
    assert res.status_code == 200

def test_login_fails_no_username(client):
    res = client.post(
        url_for('login.show'),
        data=dict(password='wrongpass')
    )

    # show with no redirect
    assert 'login' in res.location

def test_login_fails_no_password(client):
    res = client.post(
        url_for('login.show'),
        data=dict(username='username')
    )

    assert 'login' in res.location


def test_login_fails_wrong_password(client):
    res = client.post(
        url_for('login.show'),
        data=dict(username='username', password='wrongpass')
    )

    assert 'login' in res.location

def test_login_fails_username_does_not_exist(client):
    res = client.post(
        url_for('login.show'),
        data=dict(username='usergnome', password='password')
    )

    assert 'login' in res.location

def test_login_succeeds(client):
    res = client.post(
        url_for('login.show'),
        data=dict(username='username', password='password')
    )

    assert 'login' not in res.location
