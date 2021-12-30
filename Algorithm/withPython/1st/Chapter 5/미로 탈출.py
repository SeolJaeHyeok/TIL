from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
print()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

    return graph[-1][-1]

print(bfs(0, 0))

print()
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111