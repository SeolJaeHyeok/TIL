import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())

# 가능한 최대 범위로 테이블 초기화
d = [[1] * i for i in range(1, 32)]

# 모든 테이블 값 1로 초기화
for i in range(2, 31):
    for j in range(1, len(d[i]) - 1):
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

# for a in d:
#     print(*a)

idx = 0 # c번째를 시작으로 아래로 진행할 때 1씩 더해줄 변수
answer = 0
for i in range(r - 1, r + w - 1):
    for j in range(c - 1, c + idx):
        answer += d[i][j]
    idx += 1

print(answer)