import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# 맵 정보 입력 받기
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

# 4방향 이동 및 방문처리 리스트, 정답 리스트
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]

def bfs(i, j):
    global count
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나면 무시
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 조건에 부합하면 큐에 추가 및 정답 리스트에 추가
            if not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                answer[nx][ny] = answer[x][y] + 1


# 시작 위치 포함
answer[0][0] = 1
bfs(0, 0)
print(answer[-1][-1])
