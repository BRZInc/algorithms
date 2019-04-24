def check_subset_sum_recursive(numbers, s):
    if sum(numbers) < s:
        return False

    return subset_sum_recursive(numbers, s, 0)

def subset_sum_recursive(numbers, s, index):
    if len(numbers) <= index:
        return False

    if numbers[index] == s:
        return True

    if numbers[index] <= s:
        return subset_sum_recursive(numbers, s - numbers[index], index + 1)

    return subset_sum_recursive(numbers, s, index + 1)

def check_subset_sum_topdown(numbers, s):
    if sum(numbers) < s:
        return False

    mem = []
    for i in range(s + 1):
        row = [None] * (s + 1)
        mem.append(row)
    return subset_sum_topdown(mem, numbers, s, 0)

def subset_sum_topdown(mem, numbers, s, index):
    if len(numbers) <= index:
        return False

    if numbers[index] == s:
        return True

    if mem[index][s]:
        return True

    if numbers[index] <= s:
        mem[index][s] = subset_sum_topdown(mem, numbers, s - numbers[index], index + 1)
        return mem[index][s]

    mem[index][s] = subset_sum_topdown(mem, numbers, s, index + 1)
    return mem[index][s]

def check_subset_sum_bottomup(numbers, s):
    if sum(numbers) < s:
        return False

    mem = []
    for i in range(len(numbers)):
        row = [0] * (s + 1)
        mem.append(row)

    for rem in range(1, s + 1):
        if numbers[0] <= s:
            mem[0][rem] = numbers[0]

    for i in range(1, len(numbers)):
        for rem in range(1, s + 1):
            if numbers[i] > rem:
                mem[i][rem] = mem[i - 1][rem]
            else:
                mem[i][rem] = numbers[i] + mem[i - 1][rem - numbers[i]]
                if mem[i][rem] == s:
                    return True

    return False
