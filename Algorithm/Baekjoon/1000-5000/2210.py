import sys
input = sys.stdin.readline

def dfs(x, y, s):
    if len(s) == 6:
        answer.add(s)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, s + board[nx][ny])


board = []
for _ in range(5):
    board.append(list(input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(answer))


# 2, 백트래킹
import sys
input = sys.stdin.readline


def dfs(x, y, s):
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return

    if len(s) == 6:
        answer.add(s)
        return

    dfs(x + 1, y, s + board[x][y])
    dfs(x - 1, y, s + board[x][y])
    dfs(x, y + 1, s + board[x][y])
    dfs(x, y - 1, s + board[x][y])



board = []
for _ in range(5):
    board.append(list(input().split()))

answer = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(answer))