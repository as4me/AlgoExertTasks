def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            break
        currentChangeCreated += coin
    return currentChangeCreated + 1

coins = [1,2,5]
print(nonConstructibleChange(coins))