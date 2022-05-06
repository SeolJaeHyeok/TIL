import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
target = [input().rstrip() for _ in range(k)]

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

answer = defaultdict(int)
def dfs(x, y, t):
    # 해당 문자열의 등장 횟수 1 증가
    answer[t] += 1

    # 신이 좋아하는 문자의 길이는 최대 5글자
    if len(t) == 5:
        return

    # 상하좌우대각까지 모든 방향 탐색
    for i in range(8):
        nx = (x + dx[i]) % n # 격자의 범위가 n을 벗어나면 0으로
        ny = (y + dy[i]) % m # 격자의 범위가 m을 벗어나면 0으로

        # 이전 문자열에 이동할 방향의 문자열을 더해서 탐색
        dfs(nx, ny, t + board[nx][ny])

# 모든 좌표에서 탐색 시작
for i in range(n):
    for j in range(m):
        dfs(i, j, board[i][j])

# 신이 좋아하는 문자열의 횟수 출력
for t in target:
    print(answer[t])