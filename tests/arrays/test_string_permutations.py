from arrays.string_permutations import permute_string_builtin, permute_string_iteratively
import pytest


@pytest.mark.parametrize("input, expected", [
    ("ab", ["ab", "ba"]),
    ("bad", ["bad", "bda", "abd", "adb", "dab", "dba"]),
    ("izza", ['izza', 'izaz', 'izza', 'izaz', 'iazz', 'iazz', 'ziza', 'ziaz', 'zzia', 'zzai', 'zaiz', 'zazi', 'ziza', 'ziaz', 'zzia', 'zzai', 'zaiz', 'zazi', 'aizz', 'aizz', 'aziz', 'azzi', 'aziz', 'azzi'])
])
def test_permutations(input, expected):
    res1 = permute_string_builtin(input)
    res2 = permute_string_iteratively(input)
    assert set(res1) == set(expected)
    assert set(res2) == set(expected)
