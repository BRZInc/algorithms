def check_subset_partition_sum_equality_recursion(numbers):
    # Check if sum is odd.
    # In this case we won't be able to partition them equally
    total = sum(numbers)
    if total % 2 != 0:
        return False

    return partition_sum_recursively(numbers, total/2, 0)

def partition_sum_recursively(numbers, partition_sum, index):
    if index == len(numbers):
        return False

    if partition_sum - numbers[index] == 0:
        return True

    res1 = res2 = False
    if numbers[index]<=partition_sum:
        if partition_sum_recursively(numbers, partition_sum - numbers[index], index + 1):
            return True

    return partition_sum_recursively(numbers, partition_sum, index + 1)

def check_subset_partition_sum_equality_topdown(numbers):
    # Check if sum is odd.
    # In this case we won't be able to partition them equally
    total = sum(numbers)
    if total % 2 != 0:
        return False
    partition_sum = int(total / 2)

    decision_matrix = []
    for i in range(len(numbers)):
        cap = [None] * (partition_sum + 1)
        decision_matrix.append(cap)

    return partition_sum_topdown(decision_matrix, numbers, partition_sum, 0)

def partition_sum_topdown(dm, numbers, partition_sum, index):
    if index == len(numbers):
        return False

    if partition_sum - numbers[index] == 0:
        return True

    res1 = res2 = False
    if dm[index][partition_sum] is None:
        if numbers[index]<=partition_sum:
            if partition_sum_topdown(dm, numbers, partition_sum - numbers[index], index + 1):
                dm[index][partition_sum] = True
                return True
    else:
        return dm[index][partition_sum]

    dm[index][partition_sum] = partition_sum_topdown(dm, numbers, partition_sum, index + 1)
    return dm[index][partition_sum]

def check_subset_partition_sum_equality_bottomup(numbers):
    if len(numbers) <= 1:
        return False
    
    # Check if sum is odd.
    # In this case we won't be able to partition them equally
    total = sum(numbers)
    if total % 2 != 0:
        return False
    partition_sum = total // 2

    decision_matrix = []
    for i in range(len(numbers)):
        cap = [None] * (partition_sum + 1)
        cap[0] = 0
        decision_matrix.append(cap)

    for s in range(1, partition_sum + 1):
        decision_matrix[0][s] = numbers[0] if numbers[0] <= partition_sum else 0

    for i in range(1, len(numbers)):
        for s in range(1, partition_sum + 1):
            if numbers[i] > s:
                decision_matrix[i][s] = decision_matrix[i-1][s]
            else:
                decision_matrix[i][s] = numbers[i]+decision_matrix[i-1][s-numbers[i]]

    return decision_matrix[len(numbers)-1][partition_sum] == partition_sum
