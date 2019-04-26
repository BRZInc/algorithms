from recursion.typical_recursion import print_list_recursively, check_palindrome, power_calculation, generate_pascals_triangle
import pytest


def test_print_list_recursively(capfd):
    arr = [1, 2, 3, 5, 6, 7, 9]
    print_list_recursively(arr)

    out, err = capfd.readouterr()
    assert out == '1\n2\n3\n5\n6\n7\n9\n'

@pytest.mark.parametrize("input, expected", [
    ("abba", True),
    ("abcba", True),
    ("abcda", False),
    ("", True),
    ("a", True),
    ("aa", True),
    ("abcddcba", True)])
def test_check_palindrome(input, expected):
    l = len(input)
    res = check_palindrome(input, l, 0)

    assert res == expected

@pytest.mark.parametrize("number, power, expected", [
    (2, 10, 1024),
    (2, 5, 32),
    (10, 3, 1000),
    (2, 1, 2),
    (2, 0, 1)])
def test_power_calculation(number, power, expected):
    res = power_calculation(number, power)

    assert res == expected

@pytest.mark.parametrize("num_rows, expected", [
    (1, [[1]]),
    (2, [[1],[1,1]]),
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (6, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]])])
def test_generate_pascals_triangle(num_rows, expected):
    res = generate_pascals_triangle(num_rows)

    assert res == expected