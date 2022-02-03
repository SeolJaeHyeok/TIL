import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n = int(input())
score = [1, 5, 10, 50]

array = list(combinations_with_replacement(score, n)) # 가능한 중복조합의 모든 경우의 수
answer = set()
tmp = 0
# 모든 경우를 탐색
for i in range(len(array)):
    # 모든 조합의 합계를 구한 뒤 중복없이 저장
    tmp += sum(array[i])
    answer.add(tmp)
    tmp = 0

print(len(answer))