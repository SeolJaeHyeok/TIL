# 1
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 현재 위치까지 도달할 수 있는 방법의 수
d = [[0] * n for _ in range(n)]

d[0][0] = 1
for i in range(n):
    for j in range(n):
        # 마지막 값이 아니면서 현재 위치까지 도달할 방법이 있는 경우
        if board[i][j] != 0 and d[i][j] != 0:
            # 1. 아래로 이동
            if i + board[i][j] < n:
                d[i + board[i][j]][j] += d[i][j]
            # 2. 오른쪽으로 이동 가능한 경우
            if j + board[i][j] < n:
                d[i][j + board[i][j]] += d[i][j]

print(d[-1][-1])


# 2, refactoring
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
# 현재 위치까지 도달할 수 있는 방법의 수
d = [[0] * n for _ in range(n)]

d[0][0] = 1
for y in range(n):
    for x in range(n):
        # 범위를 벗어나면 탈출
        if y == n - 1 and x == n - 1:
            break

        ny = y + board[y][x] # 아래로 이동한 후 좌표
        nx = x + board[y][x] # 오른쪽으로 이동한 후 좌표

        # 아래로 이동 후 범위를 벗어나지 않으면
        if ny < n:
            # 이전까지의 값을 더해주기
            d[ny][x] += d[y][x]
        # 오른쪽으로 이동 후 범위를 벗어나지 않으면
        if nx < n:
            # 이전까지의 값을 더해주기
            d[y][nx] += d[y][x]

print(d[-1][-1])