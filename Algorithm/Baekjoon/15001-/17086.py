import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# for i in board:
#     for j in i:
#         print(j, end=' ')
#     print()

# 상어 위치 큐에 추가
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j]:
            q.append((i, j))


# 이동 방향 정의 - 8가지 방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    board[nx][ny] = board[x][y] + 1


bfs()

# for i in board:
#     for j in i:
#         print(j, end=' ')
#     print()

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, board[i][j])

print(answer - 1)

