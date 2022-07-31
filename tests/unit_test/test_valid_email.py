from server import check_email
import pytest


def test_email_found():
    club = check_email("john@simplylift.co")
    assert club["name"] == "Simply Lift"