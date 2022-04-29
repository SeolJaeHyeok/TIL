"""
n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다.
이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다.
탈출 가능한 경로의 최단 거리를 출력하는 코드를 작성해보세요.

Input
5 5                 5 5
1 0 1 1 1           1 1 1 1 1
1 0 1 0 1           1 0 1 0 1
1 0 1 1 1           1 1 1 1 1
1 0 1 0 1           1 0 1 0 1
1 1 1 0 1           1 1 1 0 1

Output
12                  8
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    global answer
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))


bfs(0, 0)

if board[-1][-1] == 1:
    print(-1)
else:
    print(board[-1][-1] - 1)
