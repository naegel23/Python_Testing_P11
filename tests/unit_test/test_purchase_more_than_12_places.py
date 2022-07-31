from server import check_available_points


def test_purchase_more_than_12_places():
    check, club, competition = check_available_points("Spring Festival", "Simply Lift", 14)
    assert check == True
    assert "you can't book more than 12 places"
