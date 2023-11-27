import pytest

def increment(x):
    x += 1
    return x

def test_increment():
    assert increment(1) == 2
