import pytest

def multiply(x,y):
    return x*y

def test_multiply_without_parameter():
    assert multiply(1,1) == 1
    assert multiply(2,2) == 4
    assert multiply(3,3) == 9

@pytest.mark.parametrize(
    "x,y, expected_output",
    [(1,1,1),(2,2,4),(3,3,9)]
)

def test_multiply_with_parameter(x,y, expected_output):
    assert multiply(x,y) == expected_output
