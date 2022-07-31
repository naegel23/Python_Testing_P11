from server import check_email
import pytest


def test_email_not_found():
    with pytest.raises(IndexError):
        check_email("example@email.com")