import sys
input = sys.stdin.readline
mod = int(1e9 + 7)

n, m = map(int, input().split())
d = [[0] * (m + 1) for _ in range(n + 1)]

d[1][1] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j != 1:
            d[i][j] = d[i-1][j-1] + d[i-1][j] + d[i][j-1]

print(d[n][m] % mod)
