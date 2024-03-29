"""
n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다.
이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다.
이 때 뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.

Input
5 5                 5 5
1 0 1 1 1           1 0 1 1 1
1 0 1 0 1           1 0 1 0 1
1 0 1 1 1           1 1 1 0 1
1 0 1 0 1           1 0 1 1 0
1 1 1 0 1           0 1 1 0 1

Output
    1                   0
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


bfs(0, 0)

print(visited[-1][-1])
