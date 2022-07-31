from server import competitions_date


def test_book_competition_date_valid_and_invalid():
    competition = competitions_date()
    competition01 = competition[0]
    competition02 = competition[2]
    assert competition01['status'] == 'invalid'
    assert competition02['status'] == 'valid'
