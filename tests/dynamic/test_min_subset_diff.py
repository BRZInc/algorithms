from dynamic.min_subset_diff import min_subset_diff_recursive, min_subset_diff_topdown
import pytest

# {1,2,3,9} => 3 {1,2,3} {9}
# {5,2,4,1} => 0 {5,1} {2,4}
# {2} => 2 {} {2}
# {} => 0 {} {}
# {1,1,4,7,11} => 0 {1,4,7} {1, 11}
@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 9], 3),
    ([5, 2, 4, 1], 0),
    ([2], 2),
    ([], 0),
    ([1, 1, 4, 7, 11], 0)])
def test_min_subset_diff_common(numbers, expected):
    res1 = min_subset_diff_recursive(numbers)
    res2 = min_subset_diff_topdown(numbers)
    assert res1 == expected
    assert res2 == expected