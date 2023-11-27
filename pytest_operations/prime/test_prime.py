import pytest

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def test_prime_numbers():
    assert is_prime(2)
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(1)



@pytest.mark.parametrize(
    "number, expected_result",
    [(2, True), (7, True), (4, False), (1, False)]
)
def test_prime_numbers_parametrized(number, expected_result):
    assert is_prime(number) == expected_result
