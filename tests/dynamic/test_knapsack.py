from dynamic.knapsack import maximum_sum_bruteforce
from datetime import datetime
import pytest


@pytest.fixture
def weights():
    return [1, 3, 2, 6]


@pytest.fixture
def costs():
    return [3, 1, 6, 8]


@pytest.mark.parametrize("capacity, expected",
    [(7, 11), (0, 0), (6, 10), (20, 18)])
def test_knapsack_bruteforce_positive(weights, costs, capacity, expected):
    res = maximum_sum_bruteforce(weights, costs, capacity=capacity)
    assert res == expected


def test_knapsack_bruteforce_empty_selection():
    res = maximum_sum_bruteforce([], [], capacity=7)
    assert res == 0

def test_knapsack_on_big_list():
    from knapsack_test_data import weights, profits

    capacity = 1000
    t1 = datetime.now()
    res = maximum_sum_bruteforce(weights, profits, capacity)
    t2 = datetime.now()

    print(t2-t1)

    assert res > 0
