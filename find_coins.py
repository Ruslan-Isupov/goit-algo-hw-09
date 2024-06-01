import timeit

def time_counter(func,data,sum):
    start = timeit.default_timer()
    result = func(sum,data)
    time_difference = timeit.default_timer() - start
    return "{:.5f}".format(time_difference), result

# Greedy_algorithms
def find_coins_greedy(sum,coins):
    coins_count ={}

    for coin in coins:
        count = sum//coin
      
        if count > 0:
            coins_count[coin] = count
           
        sum -= coin * count
        
    
    return coins_count


# Dynamic_algorithms
def find_coins_dynamic(sum,coins):
    min_coins = [0] + [float('inf')] * sum
    coins_used = [0] * (sum + 1)
    
    for i in range(1, sum + 1):
        for coin in coins:
       
            if i >= coin and min_coins[i-coin] +1 < min_coins[i]:
                min_coins[i] =  min_coins[i-coin] + 1
                coins_used[i] = coin
    
    result = {}

    current_sum = sum
    while current_sum > 0:
        coin = coins_used[current_sum]
        result[coin] = result.get(coin, 0) + 1
        current_sum -= coin

    return dict(sorted(result.items()))
    # return result


# sum = 113
# sum = 155
sum = 540
# sum = 1253
coins = [50, 25, 10, 5, 2, 1]

print("Greedy_algorithms",time_counter(find_coins_greedy,coins,sum))
print("Dynamic_algorithms",time_counter(find_coins_dynamic,coins,sum))
