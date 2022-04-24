import sys
input = sys.stdin.readline

coin = int(input())

result = 0
if coin == 1 or coin == 3:
    result = -1
elif (coin % 5) % 2 == 0:
    result = coin // 5 + (coin % 5) // 2
else:
    result = (coin // 5 - 1) + (coin % 5 + 5) // 2

print(result)