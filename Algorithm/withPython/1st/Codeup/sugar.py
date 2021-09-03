h, w = map(int, input().split())
n = int(input())
matrix = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            matrix[x-1][y-1+j] = 1
    else:
        for j in range(l):
            matrix[x-1+j][y-1] = 1

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
