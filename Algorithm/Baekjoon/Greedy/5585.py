# 5585
refund = 1000 - int(input())
array = [500, 100, 50, 10, 5, 1]

count = 0
for coin in array:
    count += refund // coin
    refund %= coin

print(count)