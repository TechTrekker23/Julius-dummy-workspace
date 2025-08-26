import math

def test_basic_math():
    assert 2 + 2 == 4

def test_sqrt():
    assert math.isclose(math.sqrt(16), 4.0)


def test_always_true():
    assert True
