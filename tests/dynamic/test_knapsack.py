from dynamic.knapsack import maximum_sum_bruteforce, maximum_sum_memoization, maximum_sum_bottomup
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

@pytest.mark.skip(reason="This test is failing due to long recursion chain")
def test_knapsack_bruteforce_on_big_list():
    from knapsack_test_data import weights, profits

    capacity = 1000
    t1 = datetime.now()
    res = maximum_sum_bruteforce(weights[:100], profits[:100], capacity)
    t2 = datetime.now()

    print(t2-t1)

    assert res > 0

@pytest.mark.parametrize("capacity, expected",
    [(7, 11), (0, 0), (6, 10), (20, 18)])
def test_knapsack_memoized_positive(weights, costs, capacity, expected):
    res = maximum_sum_memoization(weights, costs, capacity=capacity)
    assert res == expected

def test_knapsack_memoized_empty_selection():
    res = maximum_sum_memoization([], [], capacity=7)
    assert res == 0

@pytest.mark.skip(reason="This test is failing due to long recursion chain")
def test_knapsack_memoized_on_big_list():
    from knapsack_test_data import weights, profits

    capacity = 1000
    t1 = datetime.now()
    res = maximum_sum_memoization(weights[:100], profits[:100], capacity)
    t2 = datetime.now()

    print(t2-t1)

    assert res > 0

@pytest.mark.parametrize("capacity, expected",
    [(7, 11), (0, 0), (6, 10), (20, 18)])
def test_knapsack_bottomup_positive(weights, costs, capacity, expected):
    res = maximum_sum_bottomup(weights, costs, capacity=capacity)
    assert res == expected

def test_knapsack_bottomup_empty_selection():
    res = maximum_sum_bottomup([], [], capacity=7)
    assert res == 0

def test_knapsack_bottomup_non_equal_lengths(weights, costs):
    res = maximum_sum_bottomup(weights, costs[:-2], capacity=7)
    assert res == 0

def test_knapsack_bottomup_first_bigger(costs):
    weights = [8, 1, 6, 3]
    # [3, 1, 6, 8]
    res = maximum_sum_bottomup(weights, costs, capacity=7)
    assert res == 9

#@pytest.mark.skip(reason="This test is failing due to long recursion chain")
def test_knapsack_bottomup_on_big_list():
    from knapsack_test_data import weights, profits

    capacity = 1000
    t1 = datetime.now()
    res = maximum_sum_bottomup(weights, profits, capacity)
    t2 = datetime.now()

    print(t2-t1)

    assert res > 0
