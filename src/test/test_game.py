from src.web.views.games import *

def test_add(client):
    res = client.get(url_for('games.add'))
    assert res.status_code == 200
