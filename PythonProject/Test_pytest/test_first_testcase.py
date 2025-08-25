import pytest


def test_verify_login_fuctionality():
    a = 10
    assert a==10

@pytest.mark.google
def test_verify_sign_up_functionality():
    name ="Akash"

    assert name == "Akash"