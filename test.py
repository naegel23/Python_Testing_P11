from server import check_email, competitions_date, check_available_points
import pytest, requests


def test_email_not_found():
    with pytest.raises(IndexError):
        check_email("example@email.com")


def test_email_found():
    club = check_email("john@simplylift.co")
    assert club["name"] == "Simply Lift"


def test_book_competition_date_valid_and_invalid():
    competition = competitions_date()
    competition01 = competition[0]
    competition02 = competition[2]
    assert competition01['status'] == 'invalid'
    assert competition02['status'] == 'valid'


def test_purchase_places_error():
    check, club, competition = check_available_points("Spring Festival", "Simply Lift", 20)
    assert check == True
    assert "You don't have enough points available"


def test_purchase_places_valid():
    check, club, competition = check_available_points("Spring Festival", "Simply Lift", 2)
    assert check == False
    assert competition["numberOfPlaces"] == 23
    assert club["points"] == 7


def test_purchase_more_than_12_places():
    check, club, competition = check_available_points("Spring Festival", "Simply Lift", 14)
    assert check == True
    assert "you can't book more than 12 places"


def test_index_url():
    assert 200 == requests.get('http://localhost:5000').status_code


def test_show_summary_url():
    assert 200 == requests.post("http://localhost:5000/showSummary", {"email": "john@simplylift.co"}).status_code


def test_book_url():
    assert 200 == requests.get("http://localhost:5000/book/Spring%20Festival/Simply%20Lift").status_code


def test_purchase_places_url():
    assert 200 == requests.post("http://localhost:5000/purchasePlaces",
                                {"club": "Simply Lift", "competition": "Spring Festival",
                                 "places": "3"}).status_code


def test_logout_url():
    assert 200 == requests.get("http://localhost:5000/logout").status_code
