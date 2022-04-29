"""
숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 구하는 프로그램을 작성해보세요.
숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 해당 칸이 이동할 수 없는 곳임을 의미합니다.

Input
3 2         4 2
0 0 0       0 1 0 0
0 0 1       0 1 0 0
1 0 0       0 1 1 1
1 1         0 1 0 0
1 2         1 4
            4 4

Output
7           6
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    global answer
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                answer += 1


answer = 0
for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if not visited[x][y]:
        visited[x][y] = True
        answer += 1
        bfs(x, y)

print(answer)
