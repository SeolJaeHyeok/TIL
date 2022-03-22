import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# d[x][y][0] = 가로, d[x][y][1] = 세로, d[x][y][2] = 대각
d = [[[0] * 3 for _ in range(n)] for _ in range(n)]

d[0][1][0] = 1 # 시작 위치는 (0, 0) ~ (0, 1)까지 가로로 놓여있음
# 첫 번째 행은 가로로만 이동 가능
for i in range(1, n):
    if board[0][i] == 1:
        break
    d[0][i][0] = 1

for i in range(1, n):
    for j in range(2, n):
        # board[i][j] = 파이프의 끝에 위치하는 좌표
        if board[i][j] == 0:
            # 가로 방향으로 파이프를 (i, j)로 옮기는 경우 = (i, j - 1)에 가로로 도달한 경우 + (i, j - 1)에 대각선으로 도달한 경우
            d[i][j][0] = d[i][j - 1][0] + d[i][j - 1][2]
            # 세로 방향으로 파이프를 (i, j)로 옮기는 경우 = (i - 1, j)에 세로로 도달한 경우 + (i - 1, j)에 대각선으로 도달한 경우
            d[i][j][1] = d[i - 1][j][1] + d[i - 1][j][2]

        # 대각선으로 파이프를 옮기는 경우는 해당 좌표 뿐만 아니라 왼쪽과 위쪽 좌표도 비어있어야 하므로 추가로 검증
        if board[i][j] == 0 and board[i - 1][j] == 0 and board[i][j - 1] == 0:
            # 대각 방향으로 파이프를 (i, j)로 옮기는 경우
            # (i - 1, j - 1)에 가로로 도달한 경우 + (i - 1, j - 1)에 세로으로 도달한 경우 + (i - 1, j - 1)에 대각선으로 도달한 경우
            d[i][j][2] = d[i - 1][j - 1][0] + d[i - 1][j - 1][1] + d[i - 1][j - 1][2]

print(sum(d[n - 1][n - 1]))