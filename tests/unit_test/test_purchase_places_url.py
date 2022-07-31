import requests


def test_purchase_places_url():
    assert 200 == requests.post("http://localhost:5000/purchasePlaces",
                                {"club": "Simply Lift", "competition": "Spring Festival",
                                 "places": "3"}).status_code
