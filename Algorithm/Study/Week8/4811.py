d = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    d[0][i] = 1

for i in range(1, 31):
    for j in range(i, 31):
        d[i][j] += d[i-1][j] + d[i][j-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(d[n][n])

