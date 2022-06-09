import sys
input = sys.stdin.readline

n = int(input())
d = [1e9] * (n + 1)

num = 0
idx = 1
nums = []
while num < n:
    tmp = (idx * (idx + 1)) // 2
    num += tmp
    nums.append(num)
    idx += 1

for i in range(1, n + 1):
    for num in nums:
        if num == i:
            d[i] = 1
            break
        if num > i:
            break
        d[i] = min(d[i], d[i - num] + 1)

print(d[n])