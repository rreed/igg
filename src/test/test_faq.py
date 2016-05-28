import pytest

from flask import url_for

def test_show(client):
    res = client.get(url_for('faq.show'))
    assert res.status_code == 200
