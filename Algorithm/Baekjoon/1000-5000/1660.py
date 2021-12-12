# 실패
# n = int(input())
#
# d = [0] * 1000
# d[1] = 1
# d[2] = 3
# a = [0, 1]
# for i in range(3, len(d)):
#     d[i] = d[i-1] + i
#     a.append(sum(d[:i]))
#
# idx = 0
# for i in range(len(a) - 1, 0, -1):
#     if a[i] <= n:
#         idx = i
#         break
#
# array = a[:idx + 1]
# print(array)
# answer = []
# for i in range(1, len(array)):
#     count = 0
#     tmp = 0
#     while True:
#         for j in range(len(array)-1, 1, -1):
#             if tmp == n:
#                 break
#             else:
#                 tmp += array[j]
#                 count += 1
#
#
#     print(tmp)
#     # if tmp == n:
#     #     answer.append(count)
#
# print(answer)


# 다른 사람 풀이
import sys

N = int(sys.stdin.readline())
nums = []
num = 0
idx = 1
while num < N:
    num += (idx * (idx + 1)) // 2
    nums.append(num)
    idx += 1

dp = [float('inf')] * (N + 1)
for i in range(1, N + 1):
    for num in nums:
        if num == i:
            dp[i] = 1
            break
        if num > i:
            break
        dp[i] = min(dp[i], 1 + dp[i - num])

print(dp[N])