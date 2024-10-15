from bubble_sort import bubble_sort
import pytest


@pytest.mark.parametrize("lst", [[]])
def test_bubble_sort(lst):
    assert bubble_sort(lst) == []


@pytest.mark.parametrize("lst", [[1]])
def test_bubble_sort_2(lst):
    assert bubble_sort(lst) == [1]


def test_bubble_sort_3():
    unordered = [2, 65, 9, 5, 124, 1, 20]
    expected = sorted(unordered)
    assert bubble_sort(unordered) == expected


def test_bubble_sort_4():
    original = [1, 7, 3, 8, 0]
    expected = original.copy()
    assert original == expected
