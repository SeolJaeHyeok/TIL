import sys
from collections import deque
input = sys.stdin.readline

# 6가지 이동 방향 정의
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어날 경우 무시
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            # 방문하지 않은 경로라면 기존 값에 1을 더하고 큐에 추가
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


n = int(input())
x1, y1, x2, y2 = map(int, input().split())
visited = [[-1] * n for _ in range(n)]

bfs(x1, y1)
print(visited[x2][y2])