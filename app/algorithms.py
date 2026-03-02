
from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """A simple insertion sort implementation (in-place)."""
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def linear_search(arr: List[int], target: int) -> int:
    """Return index of target in arr, or -1 if not found."""
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1
