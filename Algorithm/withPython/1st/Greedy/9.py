# 동전 0, 11047
n, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

count = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if array[i] > k:
        continue
    count += k // array[i]
    k %= array[i]

print(count)
