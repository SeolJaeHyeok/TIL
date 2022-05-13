# 1, Fail
import sys
from itertools import combinations
import copy
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

# 짝수로 이루어져 있는 부분 수열 찾는 함수
def check(arr):
    d = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i - 1, i):
            if arr[i] % 2 == 0:
                d[i] = max(d[i], d[j] + 1)

    return d

for i in range(1, k + 1):
    comb = list(combinations(arr, i))

    for com in comb:
        tmp = copy.deepcopy(arr)
        for c in reversed(com):
            if tmp:
                tmp.remove(tmp[c - 1])

        answer = max(answer, max(check(tmp)))

print(answer)

# 2, Sol
n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i] %= 2
    for j in range(k + 1):
        if s[i] == 0:  # 짝수일 때
            dp[i][j] = dp[i - 1][j] + 1

        if j != 0 and s[i]:  # 홀수일 때
            dp[i][j] = dp[i - 1][j - 1]


result = []
for i in dp:
    result.append(i[k])

print(max(result))