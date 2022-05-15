import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and board[nx][ny] == '#':
                visited[nx][ny] = True
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == '#':
                bfs(i, j)
                count += 1
    print(count)