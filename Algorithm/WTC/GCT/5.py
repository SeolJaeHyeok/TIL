# sol
def solution(gold_prices):
    stock = [0] * len(gold_prices) # 주식을 가지고 있을 때 i번째 날의 이익
    not_stock = [0] * len(gold_prices) # 주식을 가지고 있지 않을 때 i번째 날의 이익

    stock[0] = -gold_prices[0] # 주식을 가지고 있을 경우 -> 첫 날은 주식 가격만큼 손해
    not_stock[0] = 0 # 주식을 가지고 있지 않을 경우 -> 첫 날은 손해 0

    for i in range(1, len(gold_prices)):
        stock[i] = max(not_stock[i - 2] - gold_prices[i], stock[i - 1])
        not_stock[i] = max(stock[i - 1] + gold_prices[i], not_stock[i - 1])

    return not_stock[-1]

print(solution([2, 5, 1, 3, 4]))
print(solution([7, 2, 5, 6, 1, 4, 2, 8]))
