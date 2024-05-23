def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Масив для відслідковування монет, що використовуються для досягнення суми
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    # Відновлення рішення
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Приклад використання
amount = 113

# Жадібний алгоритм
greedy_result = find_coins_greedy(amount)
print("Жадібний алгоритм:")
print(greedy_result)

# Динамічне програмування
dp_result = find_min_coins(amount)
print("\nДинамічне програмування:")
print(dp_result)
