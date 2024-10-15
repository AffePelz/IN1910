import pytest
from median import median


def test_median_1():
    with pytest.raises(ValueError):
        median([])


def test_median_2():
    assert median([1]) == 1


def test_median_3():
    lst = [3, 5]
    expected = 4
    assert median(lst) == expected


def test_median_4():
    lst = [11, 3, 1, 5, 3]
    expected = 3
    assert median(lst) == expected


def test_median_5():
    with pytest.raises(ValueError):
        median(())
