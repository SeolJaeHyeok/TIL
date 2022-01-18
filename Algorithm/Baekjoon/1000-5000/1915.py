import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
d = [[0] * (m + 1) for _ in range(n + 1)]

flag = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i-1][j-1] == 1:
            d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

        if d[i][j] > flag:
            flag = d[i][j]

print(flag**2)