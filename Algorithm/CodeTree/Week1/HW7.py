"""
n * n크기의 직사각형의 가운데에서 시작하여 오른쪽, 위, 왼쪽, 아래 순서로 더 이상 채울 곳이 없을 때까지 회전하며 숫자를 적어나가려고 합니다.
숫자는 1부터 시작한다고 했을 때, 다음과 같은 모양으로 숫자들을 쭉 채우는 코드를 작성해보세요.

ex)
17  16  15  14  13
18  5   4   3   12
19  6   1   2   11
20  7   8   9   10
21  22  23  24  25
"""
# My
import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]

# 시작 좌표, 진행 방향, 진행 방향에 따라 이동할 횟수 초기화
x, y, dir, move_num = n // 2, n // 2, 0, 1
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

num = 1 # 이동하면서 추가될 값
# 범위를 벗어나지 않으면 반복
while not (x < 0 or x >= n or y < 0 or y >= n):
    # 진행 방향에 따라 이동할 횟수만큼 반복
    for _ in range(move_num):
        # 값 채워넣고
        board[x][y] = num
        # 값 1 증가
        num += 1
        # 좌표 바꿔주기
        x = x + dx[dir]
        y = y + dy[dir]

        # 이동 좌표가 범위를 벗어나면 종료
        if x < 0 or x >= n or y < 0 or y >= n:
            break

    # 방향에 따른 이동 횟수를 다 이동했다면 방향 전환
    dir = (dir + 1) % 4

    # 왼쪽과 오른쪽 방향으로 이동할 때 횟수가 1씩 증가
    if dir % 2 == 0:
        move_num += 1

for b in board:
    print(*b)

# Sol
n = int(input())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 시작 위치와 방향,
# 해당 방향으로 이동할 횟수를 설정합니다.
curr_x, curr_y = n // 2, n // 2
move_dir, move_num = 0, 1


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 한 칸 움직이며 청소를 진행합니다.
def move():
    global curr_x, curr_y

    # 문제에서 원하는 진행 순서대로
    # 오른쪽 위 왼쪽 아래 방향이 되도록 정의합니다.
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    curr_x, curr_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]


def end():
    return not in_range(curr_x, curr_y)


# 시작 위치와 방향,
# 해당 방향으로 이동할 횟수를 설정합니다.
cnt = 1

while not end():
    # move_num 만큼 이동합니다.
    for _ in range(move_num):
        grid[curr_x][curr_y] = cnt
        cnt += 1

        move()

        # 이동하는 도중 격자를 벗어나게 되면,
        # 움직이는 것을 종료합니다.
        if end():
            break

    # 방향을 바꿉니다.
    move_dir = (move_dir + 1) % 4
    # 만약 현재 방향이 왼쪽 혹은 오른쪽이 된 경우에는
    # 특정 방향으로 움직여야 할 횟수를 1 증가시킵니다.
    if move_dir == 0 or move_dir == 2:
        move_num += 1

# 출력:
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()