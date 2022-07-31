import requests


def test_show_summary_url():
    assert 200 == requests.post("http://localhost:5000/showSummary", {"email": "john@simplylift.co"}).status_code