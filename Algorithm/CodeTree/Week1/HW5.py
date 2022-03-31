"""
n * m크기의 직사각형에 숫자 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 코드를 작성해보세요.
달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 아래, 오른쪽, 위쪽, 왼쪽 순서로 더 이상 채울 곳이 없을 때까지 회전하는 모양을 의미합니다.

ex)
1   14  13  12  11
2   15  20  19  10
3   16  17  18  9
4   5   6   7   8
"""
# my
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

# 이동 방향, 초기 좌표, 진행 방향 초기화
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y, dir = 0, 0, 0

# 초기값 설정
board[x][y] = 1

# 좌표의 개수만큼 반복
for i in range(2, n * m + 1):
    # 이동할 좌표
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 이동할 좌표가 범위를 벗어나거나 이미 방문한 적이 있는 좌표라면 반시계 방향으로 90도 회전
    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 0:
        dir = (dir + 1) % 4

    # 좌표값 바꿔주고 바꾼 좌표에 값 추가
    x, y = x + dx[dir], y + dy[dir]
    board[x][y] = i

for b in board:
    print(*b)

# sol
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
answer = [
    [0] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0  # 시작은 (0, 0) 입니다.
dir_num = 1  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 처음 시작 위치에 초기값을 적습니다.
answer[x][y] = 1

# n*m번 진행합니다.
for i in range(2, n * m + 1):
    # 나아갈 수 있을때까지 방향을 바꿔가며 확인해봅니다.
    while True:
        # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        # 그 위치로 나아갈 수 있는지 확인합니다.
        if in_range(nx, ny) and answer[nx][ny] == 0:
            # 나아갈 수 있다면 위치를 갱신해주고 배열에 올바른 값을 채워넣습니다.
            x, y = nx, ny
            answer[x][y] = i
            break
        else:
            # 나아갈 수 없다면 반시계방향으로 90'를 회전하여
            # 그 다음 방향을 확인해봐야 합니다.
            dir_num = (dir_num + 3) % 4

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()