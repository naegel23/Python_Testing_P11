import requests


def test_book_url():
    assert 200 == requests.get("http://localhost:5000/book/Spring%20Festival/Simply%20Lift").status_code