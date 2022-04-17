"""
n * n크기의 이차원 영역에 사람 혹은 벽이 놓여져있습니다.
이 때 상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는 것으로 간주한다고 합니다.
이 때 총 마을의 개수와 같은 마을에 있는 사람의 수를 오름차순으로 정렬하여 출력하는 코드를 작성해보세요.

Input
5
1 0 1 1 1
1 0 0 0 0
0 0 0 1 1
1 1 0 1 1
1 1 0 1 1

Output
4
2
3
4
6
"""
# 1
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count
    # 범위를 벗어나면 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # 사람일 경우
    if board[x][y] == 1:
        count += 1  # 사람의 수 1 증가
        board[x][y] = 0  # 해당 위치 벽으로 만들어 주고

        # 상, 하, 좌, 우 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        # 시작 좌표부터 확장할 수 있는 만큼 확장한 다음 True 리턴
        return True

    # 벽일 경우 False
    return False


towns = 0  # 마을의 수
humans = []  # 마을에 속한 사람의 수
# 모든 위치에서 탐색 수행
for i in range(n):
    for j in range(n):
        count = 0
        # True를 리턴한 경우 해당 좌표를 시작점으로 하여 가능한 최대 넓이의 마을이 생성
        if dfs(i, j):
            # 따라서 마을의 수를 1 증가시키고 해당 마을의 사람 수를 추가
            towns += 1
            humans.append(count)

print(towns)
for h in sorted(humans):
    print(h)

# 2
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if board[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            count += 1

            dfs(nx, ny)


humans = []  # 마을에 속한 사람의 수
# 모든 위치에서 탐색 수행
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            count = 1
            dfs(i, j)
            humans.append(count)

print(len(humans))
for h in sorted(humans):
    print(h)
