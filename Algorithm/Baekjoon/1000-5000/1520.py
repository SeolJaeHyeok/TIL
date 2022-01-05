import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] < board[x][y]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]

print(dfs(0, 0))

"""
1. 과정을 진행하면서 visited에 저장된 값이 0이면 목적지에 도달하지 못하므로 0을 return 해준다.
2. 1 이상의 값이면 이전에 그만큼 방문 경로가 있으므로 해당 값을 반환해서 더해준다.
3. -1 이면 방문하지 않은 경로이므로 dfs 수행
출처: https://ca.ramel.be/70 [MemoLOG]
"""