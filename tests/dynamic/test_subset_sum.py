from dynamic.subset_sum import check_subset_sum_recursive, check_subset_sum_topdown, check_subset_sum_bottomup
import pytest


@pytest.mark.parametrize("numbers, s, expected", [
    ([1, 2, 3, 7], 6, True),
    ([1, 2, 7, 1, 5], 10, True),
    ([1, 3, 4, 8], 6, False),
    ([], 5, False),
    ([1, 2, 3, 4], 100, False)])
def test_subset_sum_positive(numbers, s, expected):
    res1 = check_subset_sum_recursive(numbers, s)
    res2 = check_subset_sum_topdown(numbers, s)
    res3 = check_subset_sum_bottomup(numbers, s)

    assert res1 == expected
    assert res2 == expected
    assert res3 == expected
