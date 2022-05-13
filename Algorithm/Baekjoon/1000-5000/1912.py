import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 1
d = [0] * n
d[0] = arr[0]

for i in range(n - 1):
    d[i + 1] = max(arr[i + 1], d[i] + arr[i + 1])

print(max(d))

# 2
for i in range(1, n):
    arr[i] = max(arr[i], arr[i - 1] + arr[i])

print(max(arr))