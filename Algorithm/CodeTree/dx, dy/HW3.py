"""

N * N 크기의 격자 위에 총 M번에 걸쳐 색칠을 진행합니다.
한 번에 한 칸만 색칠하며, 색칠을 한 직후 해당 칸이 '편안한 상태'에 놓여 있는지를 확인하려 합니다.
‘편안한 상태’란 방금 막 칠해진 칸을 기점으로 위 아래 양옆으로 인접한 4개의 칸 중 격자를 벗어나지 않는 칸에 색칠되어 있는 칸이 정확히 3개인 경우를 뜻합니다.
색칠할 칸이 주어질 때마다 해당 칸을 칠한 직후 막 칠한 칸이 편안한 상태에 있는지를 계속 알아내는 프로그램을 작성해보세요.
"""

# my
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# m번 반복
for _ in range(m):
    x, y = map(int, input().split())
    # 입력 받은 좌표 새칠
    board[x][y] = 1
    count = 0
    # 입력 받은 좌표를 기준으로 상,하,좌,우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나면 무시
        if nx < 0 or nx > n or ny < 0 or ny > n:
            continue
        # 상,하,좌,우의 색칠 여부 체크
        if board[nx][ny] == 1:
            count += 1

    if count == 3:  # 3곳의 좌표가 색칠이 되어있는 경우
        print(1)
    else:  # 그렇지 않은 경우
        print(0)

# sol
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1

    return cnt


for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x -= 1
    y -= 1
    arr[x][y] = 1

    # 해당 칸을 탐색합니다.
    if adjacent_cnt(x, y) == 3:
        print(1)
    else:
        print(0)