n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))