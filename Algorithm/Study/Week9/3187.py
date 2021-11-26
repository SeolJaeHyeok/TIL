from collections import deque

queue = deque()


def bfs(x, y):
    global wolf, sheep

    # 큐에 추가하고 방문처리
    queue.append([x, y])
    visited[x][y] = 1

    # 탐색
    while queue:
        x, y = queue.popleft()

        if board[x][y] == 'v':  # v면 늑대 +1
            wolf += 1
        elif board[x][y] == 'k':  # k라면 양 +1
            sheep += 1

        # 동서남북 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동한 좌표(nx, ny)가 울타리(#)가 아니고 방문하지 않은 곳이라면 큐에 추가 후 방문처리
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != '#' and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1


r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(str, input())))

# 방문 처리 리스트
visited = [[0] * c for _ in range(r)]
# 이동 방향 정의(북, 남, 서, 동)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 살아남은 양과 늑대
alive_wolf = alive_sheep = 0
# 모든 좌표를 시작점으로 하여 조건에 맞는 좌표만 bfs 탐색
for i in range(r):
    for j in range(c):
        if board[i][j] != '#' and not visited[i][j]:
            wolf = sheep = 0
            bfs(i, j)
            if wolf >= sheep:  # 탐색 후 늑대의 수가 양의 수 이상이라면 늑대의 수 증가
                alive_wolf += wolf
            else:  # 탐색 후 양의 수가 늑대의 수보다 많다면 양의 수 증가
                alive_sheep += sheep

print(alive_sheep, alive_wolf)
