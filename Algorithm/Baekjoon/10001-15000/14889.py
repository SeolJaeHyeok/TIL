# 스타트와 링크
# 데크 자료형으로 가능한 팀 조합 추출
from itertools import combinations
from collections import deque

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

temp = [i for i in range(n)]

q = deque(combinations(temp, n // 2))
min_value = 1e9

while q:
    start, link = q.popleft(), q.pop()
    value = 0
    # start 팀 합계
    for i in start:
        for j in start:
            value += array[i][j]
    # link 팀 합계
    for i in link:
        for j in link:
            value -= array[i][j]

    min_value = min(min_value, abs(value))

print(min_value)
