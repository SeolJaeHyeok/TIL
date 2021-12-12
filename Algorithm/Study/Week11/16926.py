import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        # x, y 는 돌려지는 배열중 가장 첫번째 배열 인덱스
        x, y = i, i
        temp = data[x][y]

        # 안쪽까지 계속 고려해야하기 때문에 n-i랑 m-i까지로 범위설정
        # 좌
        for j in range(i + 1, n - i):
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        # 하
        for j in range(i + 1, m - i):
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        # 우
        for j in range(i + 1, n - i):
            x = n - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        # 상
        for j in range(i + 1, m - i):
            y = m - j -1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()