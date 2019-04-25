from dynamic.coin_change import change_coins_recursively, change_coins_topdown, change_coins_bottomup
import pytest

# {1, 3, 5} => 10
# {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# {1, 1, 1, 1, 1, 1, 1, 3}
# {1, 1, 1, 1, 3, 3}
# {1, 3, 3, 3}
# {1, 1, 1, 1, 1, 5}
# {5, 5}
# {1, 1, 3, 5}
# Answer: 7

@pytest.mark.parametrize("coins, amount, ways_count", [
    ([1, 2, 3], 5, 5),
    ([1, 3, 5], 10, 7),
    ([5, 1, 3], 10, 7),
    ([3], 5, 0),
    ([5], 3, 0),
    ([1], 10, 1),
    ([], 10, 0)])
def test_change_coin_positive(coins, amount, ways_count):
    res1 = change_coins_recursively(coins, amount)
    res2 = change_coins_topdown(coins, amount)
    res3 = change_coins_bottomup(coins, amount)

    assert res1 == ways_count
    assert res2 == ways_count
    assert res3 == ways_count
