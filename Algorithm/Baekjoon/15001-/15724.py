import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

d = [[0] * (m + 1) for _ in range(n + 1)]

# 누적합 구하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = board[i - 1][j - 1] + d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1]

# 해당 범위의 총 사람 수 구하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 마지막 좌표까지의 누적합에서 한 번 겹치는 부분을 빼고 두 번 겹치는 부분은 더함
    # (1, 1) ~ (2, 3)까지의 범위를 구한다고 하면 시작 행과 열에서 -1을 해준 행과 열을 빼주고 겹치는 부분은 더해주어야 한다.
    # Why? (0, 0) ~ (n - 1, m - 1) 범위까지 이어져오면서 누적합을 구하기 때문에 위 연산을 하지 않는 경우 두 번 더해지는 경우가 생기기 때문에
    answer = d[x2][y2] - d[x1 - 1][y2] - d[x2][y1 - 1] + d[x1 - 1][y1 - 1]
    print(answer)