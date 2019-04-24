from dynamic.equal_subset import check_subset_partition_sum_equality_recursion, check_subset_partition_sum_equality_bottomup
import pytest


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], True),
    ([1, 1, 3, 4, 7], True),
    ([2, 3, 4, 6], False),
    ([1, 3, 5], False)])
def test_equal_subset_common(numbers, expected):
    res1 = check_subset_partition_sum_equality_recursion(numbers)
    res2 = check_subset_partition_sum_equality_bottomup(numbers)

    assert res1 == expected
    assert res2 == expected
