from itertools import permutations

def permute_string_builtin(s):
    return [''.join(p) for p in permutations(s)]

def permute_string_iteratively(s):
    if len(s) <= 1:
        return s
    results = []
    permute_recursively(s, 0, results)
   
    return results

def permute_recursively(s, step, results):
    if step == len(s):
        results.append(s)
        return
    
    for i in range(step, len(s)):
        swapped = swap_chars(s, step, i)
        permute_recursively(swapped, step + 1, results)
    return

def swap_chars(s, index_1, index_2):
    l = list(s)
    l[index_1], l[index_2] = l[index_2], l[index_1]
    return ''.join(l)