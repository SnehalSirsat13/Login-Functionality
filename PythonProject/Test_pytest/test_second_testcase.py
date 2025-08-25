import pytest

@pytest.mark.google
def test_sum_of_num():
    a = 10
    b = 20
    assert a+b ==30