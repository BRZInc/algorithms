def change_coins_recursively(coins, amount):
    if len(coins) == 0:
        return 0

    return process_coins_recursively(coins, amount, 0)

def process_coins_recursively(coins, amount, index):
    if amount == 0:
        return 1

    if index >= len(coins):
        return 0

    count = 0
    if coins[index] <= amount:
        count += process_coins_recursively(coins, amount - coins[index], index)
        
    count += process_coins_recursively(coins, amount, index + 1)
    return count


def change_coins_topdown(coins, amount):
    if len(coins) == 0:
        return 0

    mem = []
    for i in range(len(coins)):
        w = [None] * (amount + 1)
        mem.append(w)
    return process_coins_topdown(mem, coins, amount, 0)

def process_coins_topdown(mem, coins, amount, index):
    if amount == 0:
        return 1

    if index >= len(coins):
        return 0

    if mem[index][amount]:
        return mem[index][amount]

    count = 0
    if coins[index] <= amount:
        count += process_coins_recursively(coins, amount - coins[index], index)
        
    count += process_coins_recursively(coins, amount, index + 1)
    mem[index][amount] = count
    return mem[index][amount]

def change_coins_bottomup(coins, amount):
    if len(coins) == 0:
        return 0

    mem = []
    for i in range(len(coins)):
        w = [0] * (amount + 1)
        w[0] = 1
        mem.append(w)


    for i in range(0, len(coins)):
        for a in range(1, amount + 1):
            if i > 0:
                mem[i][a] = mem[i-1][a]
            if coins[i] <= a:
                mem[i][a] += mem[i][a-coins[i]]

    return mem[len(coins)-1][amount]
