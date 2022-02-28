import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

print(round(sum(nums) / n))
print(nums[n // 2])
arr = []
for k, v in Counter(nums).items():
    arr.append((k, v))

arr.sort(key=lambda x: x[1], reverse=True)
most = arr[0][0]
if len(arr) > 1 and arr[0][1] == arr[1][1]:
    most = arr[1][0]
print(most)
print(abs(nums[0] - nums[-1]))