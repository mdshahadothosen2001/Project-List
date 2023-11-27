import pytest

def increment(x):
    x += 1
    return x

@pytest.mark.parametrize(
    "x, expected_output",
    [(1,2),(2,3),(3,4)]
)

def test_increment(x, expected_output):
    assert increment(x) == expected_output
