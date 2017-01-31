import pytest
import bcrypt

from flask import url_for
from src.data.models import User
from src.data.db import db as _db

def setup_module(cls):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw('password', salt)
    user = User.create(username='test_admin', password=hashed_pw, email='admin@example.example', salt=salt, admin = True)
    user2 = User.create(username='test_rando', password=hashed_pw, email='rando@example.example', salt=salt, admin = False)


def teardown_module(cls):
    _db.session.query(User).filter_by(username='test_admin').delete()
    _db.session.query(User).filter_by(username='test_rando').delete()
    _db.session.commit()

def test_show_admin_index(client):
    res = client.get(url_for('admin.index'))
    assert res.status_code == 200

def test_admin_fails_while_anon(client):
    res = client.get(url_for('challengeadmin.index_view'))
    assert res.status_code == 302
    assert 'login' in res.location

def test_admin_fails_while_not_admin(client):
    client.post(url_for('login.show'), data=dict(username='test_rando', password='password'))
    res = client.get(url_for('challengeadmin.index_view'))
    assert res.status_code == 302
    assert 'login' in res.location

def test_admin_succeeds_while_admin(client):
    client.post(url_for('login.show'), data=dict(username='test_admin', password='password'))
    res = client.get(url_for('challengeadmin.index_view'))
    assert res.status_code == 200
