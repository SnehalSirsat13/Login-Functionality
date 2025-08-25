import pytest

@pytest.fixture()
def setup():
    b = 9
    yield b


def test_fun(setup):
    c = setup
    b = 10
    assert b == c
