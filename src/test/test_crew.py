import pytest

from src.web.views.games import *

def test_show(client):
    res = client.get(url_for('crew.show'))
    assert res.status_code == 200
