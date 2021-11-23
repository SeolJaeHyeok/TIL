array = [[0] * 101 for _ in range(101)]

n, m = map(int, input().split())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            array[x][y] += 1

    # for i in range(len(array)):
    #     for j in range(len(array[0])):
    #         print(array[i][j], end=' ')
    #     print()

count = 0
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] > m:
            count += 1

print(count)
