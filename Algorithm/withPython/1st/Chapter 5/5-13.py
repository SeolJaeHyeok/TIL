# 미로 탈출
from collections import deque

def bfs(x, y):
    q = deque()
    # 시작 좌표 큐에 추가
    q.append((x, y))
    # 이동할 방향 정의 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        for i in range(4):
            # 이동할 방향 정의
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 위치가 범위를 벗어나면 스킵
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 이동할 방향의 값이 0이라면(벽인 경우) 스킵
            if graph[nx][ny] == 0:
                continue
            # 이동할 방향의 값이 1이라면(방문한 적이 없다면 == 네 방향 중 이동해야할 곳이라면)
            if graph[nx][ny] == 1:
                # 이전까지의 값에 1을 더하여 최단거리 저장(이동한 거리를 계산해야되기 때문에 상, 하, 좌, 우로 이동할 경우 거리가 1이 늘어남)
                graph[nx][ny] = graph[x][y] + 1
                # 이동 후 큐에 추가
                q.append((nx, ny))

    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs(0, 0))