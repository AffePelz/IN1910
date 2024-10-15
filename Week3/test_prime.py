from Prime import is_prime
import pytest


def test_is_prime():
    with pytest.raises(ValueError):
        is_prime(-1)


def test_is_prime_2():
    for i in ("yoy", 1.1, {}, []):
        with pytest.raises(ValueError):
            is_prime(i)


def test_is_prime_3():
    for i in (2, 3, 5, 7, 11):
        assert is_prime(i)


def test_is_prime_4():
    for i in (1, 4, 6, 8, 9):
        assert not is_prime(i)
