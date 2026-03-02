
from app.algorithms import insertion_sort, linear_search


def test_insertion_sort_basic():
    assert insertion_sort([3, 1, 2]) == [1, 2, 3]


def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]


def test_linear_search_found():
    assert linear_search([1, 2, 3], 2) == 1


def test_linear_search_not_found():
    assert linear_search([1, 2, 3], 5) == -1
