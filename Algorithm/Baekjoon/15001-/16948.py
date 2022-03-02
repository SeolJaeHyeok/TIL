import sys
from collections import deque
input = sys.stdin.readline

# 6가지 이동 방향 정의
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# 1
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

            # 방문하지 않은 경로라면 이전 값에 1을 더하고 큐에 추가
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


n = int(input())
x1, y1, x2, y2 = map(int, input().split())
visited = [[-1] * n for _ in range(n)]

bfs(x1, y1)
print(visited[x2][y2])

# 2
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count = 0
    while q:
        count += 1
        # 한 정점에서 6가지 방향으로 이동 가능하지만 한 정점에서 방문할 수 있는 횟수는 1로 처리
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]

                # 목표지점에 도달했으면 시도 횟수 반환
                if nx == x2 and ny == y2:
                    return count

                # 이동 경로가 범위를 벗어나지 않고 방문하지 않았을 경우 방문처리 및 큐에 추가
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    # 목표지점에 도달하지 못한 채 큐를 빠져나왔으면 -1 반환
    return -1

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
visited = [[False] * n for _ in range(n)]

print(bfs(x1, y1))