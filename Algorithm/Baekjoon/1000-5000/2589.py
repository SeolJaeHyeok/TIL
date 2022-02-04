from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    times = 0 # 최대 시간
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동한 좌표가 범위를 벗어나면 무시
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            # 이동한 좌표를 방문하지 않고 육지인 경우 값 갱신 후 큐에 추가
            if visited[nx][ny] == 0 and board[nx][ny] != "W":
                visited[nx][ny] = 1
                board[nx][ny] = board[x][y] + 1
                times = max(times, board[nx][ny])
                q.append([nx, ny])

    return times


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input().strip()))

answer = 0
for i in range(n):
    for j in range(m):
        # 육지인 경우에만 BFS 탐색
        if board[i][j] != "W":
            # 새로운 방문처리 리스트
            visited = [[0] * m for _ in range(n)]
            # 시작값을 0으로 만든 후 방문 처리
            board[i][j] = 0
            visited[i][j] = 1
            # 탐색후 나온 최대 거리 값과 현재 값을 비교하여 갱신
            answer = max(answer, bfs(i, j))

print(answer)
