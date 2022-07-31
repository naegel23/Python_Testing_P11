from server import check_available_points


def test_purchase_places_valid():
    check, club, competition = check_available_points("Spring Festival", "Simply Lift", 2)
    assert check == False
    assert competition["numberOfPlaces"] == 23
    assert club["points"] == 7