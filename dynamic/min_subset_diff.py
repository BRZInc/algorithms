# {1,2,3,9} => 3 {1,2,3} {9}
# {5,2,4,1} => 0 {5,1} {2,4}
# {2} => 2 {} {2}
# {} => 0 {} {}
# {1,1,4,7,11} => 0 {1,4,7} {1, 11}
def min_subset_diff_recursive(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]

    return get_difference_recursively(numbers, 0, 0, 0)


def get_difference_recursively(numbers, index, sum1, sum2):
    if index == len(numbers):
        return abs(sum1 - sum2)

    diff1 = get_difference_recursively(
        numbers, index + 1, sum1 + numbers[index], sum2)
    diff2 = get_difference_recursively(
        numbers, index + 1, sum1, sum2 + numbers[index])

    return min(diff1, diff2)

def min_subset_diff_topdown(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]

    mem = []
    s = sum(numbers)
    for i in range(len(numbers)):
        r = [-1] * s
        mem.append(r)

    return get_difference_topdown(mem, numbers, 0, 0, 0)


def get_difference_topdown(mem, numbers, index, sum1, sum2):
    if index == len(numbers):
        return abs(sum1 - sum2)

    if mem[index][sum1] < 0:
        diff1 = get_difference_topdown(
            mem, numbers, index + 1, sum1 + numbers[index], sum2)
        diff2 = get_difference_topdown(
            mem, numbers, index + 1, sum1, sum2 + numbers[index])

        mem[index][sum1] = min(diff1, diff2)
    return mem[index][sum1]

def min_subset_diff_bottomup(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]

    