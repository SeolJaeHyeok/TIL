import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

# 모든 재료를 담을 리스트
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 재료를 가지고 1개 ~ n개까지 재료를 고르는 경우의 수
comb = []
for i in range(1, n + 1):
    comb.append(list(combinations(arr, i)))

answer = 1e9
for c in comb:
    for a in c:
        s = 1 # 신 맛의 합
        b = 0 # 쓴 맛의 합
        for t in a:
            s *= t[0]
            b += t[1]
        answer = min(answer, abs(s - b))

print(answer)