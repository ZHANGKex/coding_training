def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount = amount - coin
            count += 1
    return count if amount == 0 else -1

print(min_coins([1, 2, 5], 11))