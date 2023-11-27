import pytest

def increment(x):
    x += 1
    return x

def test_increment_without_parameter():
    assert increment(1) == 2
    assert increment(2) == 3
    assert increment(3) == 4

@pytest.mark.parametrize(
    "x, expected_output",
    [(1,2),(2,3),(3,4)]
)

def test_increment_with_parameter(x, expected_output):
    assert increment(x) == expected_output
