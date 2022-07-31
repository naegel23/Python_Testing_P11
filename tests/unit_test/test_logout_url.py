import requests


def test_logout_url():
    assert 200 == requests.get("http://localhost:5000/logout").status_code