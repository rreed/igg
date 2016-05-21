import pytest

from flask import url_for

def test_show(client, db):
    res = client.get(url_for('games.show'))
    assert res.status_code == 200

def test_add(client):
    res = client.get(url_for('games.add'))
    assert res.status_code == 200

def test_create(client, db):
    with pytest.raises(AssertionError):
        res = client.post(url_for('games.create'))

    res = client.post(url_for('games.create'), data=dict(name='test name', developer='test dev'))
    assert res.status_code == 302
