from server import check_available_points


def test_purchase_places_error():
    check, club, competition = check_available_points("Spring Festival", "Simply Lift", 20)
    assert check == True
    assert "You don't have enough points available"
