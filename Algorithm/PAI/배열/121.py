# Best Time to Buy and Sell Stock
# 브루트 포스, 시간 초과
def maxProfit(prices:list[int]) -> int:
    maxValue = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxValue = max(maxValue, profit)

    return maxValue


print(maxProfit([7, 1, 5, 3, 6, 4]))

# 저점과 현재 값과의 차이 계산, O(n), 1104ms
def maxProfit(prices:list[int]) -> int:
    # 최대 이익과 저점 초기화
    profit = 0
    min_price = 1e9

    for price in prices:
        # 이전 상태의 저점과 현재 값 중에 작은 값으로 저점 갱신
        min_price = min(min_price, price)
        # 그 저점을 기준으로 최대 이익 갱신
        profit = max(profit, price - min_price)

    return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))

"""
- 현재 값을 가리키는 포인터가 이전 상태의 저점을 기준으로 가격 차이를 계산하고
- 만약 클 경우 최댓값을 계속 교체해나가는 방식으로 구현 가능
"""