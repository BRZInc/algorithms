def maximum_sum_bruteforce(weights, profit, capacity=7):
    return knapsack_recursive(weights, profit, capacity, 0)


def knapsack_recursive(weights, profit, capacity, current_index):
    if capacity <= 0 or current_index >= len(weights):
        return 0

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profit[current_index] + knapsack_recursive(
            weights, profit, capacity - weights[current_index], current_index + 1)

    profit2 = knapsack_recursive(weights, profit, capacity, current_index + 1)

    return max(profit1, profit2)


def maximum_sum_memoization(weights, profit, capacity=7):
    mem = {}
    return knapsack_memoized(mem, weights, profit, capacity, 0)


def knapsack_memoized(mem, weights, profit, capacity, current_index):
    if capacity <= 0 or current_index >= len(weights):
        return 0

    if mem.get(current_index):
        if mem[current_index].get(capacity):
            return mem[current_index][capacity]

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profit[current_index] + knapsack_memoized(
            mem, weights, profit, capacity - weights[current_index], current_index + 1)

    profit2 = knapsack_memoized(mem, weights, profit, capacity, current_index + 1)

    if not mem.get(current_index):
        mem[current_index] = {}
    mem[current_index][capacity] = max(profit1, profit2)

    return mem[current_index][capacity]


def maximum_sum_bottomup(weights, profit, capacity=7):
    if capacity == 0 or len(weights) != len(profit) or len(weights) == 0 or len(profit) == 0:
        return 0

    # Init decision matrix
    decision_matrix = []
    for i in range(len(weights)):
        cap = [None] * (capacity + 1)
        cap[0] = 0
        decision_matrix.append(cap)

    for cap in range(1, capacity + 1):
        decision_matrix[0][cap] = profit[0] if weights[0] <= capacity else 0

    for i in range(1, len(weights)):
        for cap in range(1, capacity + 1):
            profit1 = profit2 = 0
            if weights[i] <= cap:
                profit1 = profit[i] + decision_matrix[i - 1][cap - weights[i]]
            
            profit2 = decision_matrix[i - 1][cap]

            decision_matrix[i][cap] = max(profit1, profit2)

    print_knapsack_contents(decision_matrix, weights, profit, capacity)

    return decision_matrix[len(weights) - 1][capacity]

def print_knapsack_contents(decision_matrix, weights, profit, capacity):
    top_value = decision_matrix[len(weights)-1][capacity]
    last_value_capacity = capacity

    values = []
    for i in range(len(weights)-1, -1, -1):
        if i == 0:
            if weights[i]==last_value_capacity:
                values.append(i)
        elif decision_matrix[i][last_value_capacity] != decision_matrix[i-1][last_value_capacity]:
            values.append(i)
            last_value_capacity = last_value_capacity - weights[i]

    print(values)
