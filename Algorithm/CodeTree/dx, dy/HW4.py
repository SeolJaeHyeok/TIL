"""
N * N 크기의 격자 안에 각 칸마다 거울이 하나씩 들어 있습니다.
각 거울은 ‘\'나 '/’의 형태를 띄고있고, 격자 밖 4N개의 위치 중 특정 위치에서 레이저를 쏘았을 때, 거울에 튕기는 횟수를 구하는 프로그램을 작성해보세요.
"""
import sys
input = sys.stdin.readline

# 시작 위치와 방향 초기화
def initialize(start):
    if start <= n:
        return 0, start - 1, 0
    elif start <= 2 * n:
        return start - n - 1, n - 1, 1
    elif start <= 3 * n:
        return n - 1, n - (start - 2 * n), 2
    else:
        return n - (start - 3 * n), 0, 3

# (x, y)에서 next_dir 방향으로 이동 후 해당 위치 반환
def move(x, y, next_dir):
    dx = [1, 0 , -1, 0]
    dy = [0, -1, 0, 1]
    nx = x + dx[next_dir]
    ny = y + dy[next_dir]
    return nx, ny, next_dir

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
start = int(input())

# 시작 좌표와 이동 방향 초기화
x, y, dir = initialize(start)

answer = 0
# 범위를 벗어나지 않으면 반복
while 0 <= x < n and 0 <= y < n:
    # 0 <-> 1 / 2 <-> 3
    # 해당 값과 1을 XOR 연산하면 위 값이 나온다.
    # XOR 연산은 각 비트가 같을 경우 0, 다른 경우 1을 만들어 주는 연산
    if board[x][y] == '/':
        x, y, dir = move(x, y, dir ^ 1)
    # 0 <-> 3 / 1 <-> 2
    else:
        x, y, dir = move(x, y, 3 - dir)

    answer += 1

print(answer)