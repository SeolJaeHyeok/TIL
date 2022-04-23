import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1

board = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

answer = -1

dx = [-1, -1, -2, -2, 1, 1, 2, 2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]
def bfs(i, j):
    global answer
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1

    # 도착점까지 도달 가능한 경우 정답 처리
    if visited[r2][c2]:
        answer = board[r2][c2]


bfs(r1, c1)

if answer == -1:
    print(-1)
else:
    print(answer)


