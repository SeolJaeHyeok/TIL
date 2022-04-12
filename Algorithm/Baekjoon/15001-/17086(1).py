import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 8가지 이동 방향 정의 11시를 시작으로 시계방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs():
    while q:
        # 현재 좌표
        x, y = q.popleft()
        # 8가지 방향 탐색
        for i in range(8):
            # 이동할 좌표
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 좌표가 범위 내에 존재하고
            if 0 <= nx < n and 0 <= ny < m:
                # 값이 0일 경우만 이동이 가능
                if board[nx][ny] == 0:
                    # 이동할 좌표의 값은 현재 좌표의 값에서 1칸 증가
                    board[nx][ny] = board[x][y] + 1
                    # 큐에 추가
                    q.append((nx, ny))


# 상어의 위치를 기준으로 8가지 방향을 탐색하면 되기 때문에 미리 모든 상어의 위치를 큐에 넣어준다.
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

bfs()

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, board[i][j])

print(answer - 1)