import pytest
from maximum_subarray_sum import maximumSubarraySum


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 5, 4, 2, 9, 9, 3], 3, 15),
    ([9, 9, 9, 1, 2, 3], 3, 12),
    ([1, 2, 3, 4, 5], 2, 9),
    ([1, 2, 1, 3], 2, 4),
    ([1, 2, 3], 3, 6),
    ([3, 1, 4, 1, 5], 1, 5),
    ([5, 5, 5], 2, 0),
    ([1, 1, 2], 3, 0),
    (list(range(1, 101)), 5, 490),
])
def test_maximumSubarraySum(nums, k, expected):
    assert maximumSubarraySum(nums, k) == expected


def test_single_element():
    assert maximumSubarraySum([42], 1) == 42


def test_all_same_elements():
    assert maximumSubarraySum([7, 7, 7, 7], 2) == 0


def test_returns_zero_when_no_valid_subarray():
    assert maximumSubarraySum([1, 1], 2) == 0
