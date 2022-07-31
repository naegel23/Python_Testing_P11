import requests


def test_index_url():
    assert 200 == requests.get('http://localhost:5000').status_code