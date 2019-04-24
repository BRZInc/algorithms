def maximum_sum_bruteforce(weights, profit, capacity=7):
	return knapsack_recursive(weights, profit, capacity, current_index=0)


def knapsack_recursive(weights, profit, capacity, current_index=0):
    if capacity <= 0 or current_index >= len(weights):
        return 0

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profit[current_index] + knapsack_recursive(
            weights, profit, capacity - weights[current_index], current_index + 1)

    profit2 = knapsack_recursive(weights, profit, capacity, current_index + 1)

    return max(profit1, profit2)