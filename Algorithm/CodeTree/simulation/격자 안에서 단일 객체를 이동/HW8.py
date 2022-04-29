"""
N*N 크기의 격자 안에서 주어진 위치에서 우측 방향을 바라보고 시작하여 오른쪽 벽을 짚고 쭉 따라가는 방식으로 미로를 탈출하는 프로그램을 작성해보세요.
규칙에 맞게 이동하다 격자 밖을 벗어났을 때 미로를 탈출 한 것으로 봅니다.

벽을 짚고 탈출하는 방식은 다음과 같습니다.

1. 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우
    1) 반 시계 방향으로 90' 만큼 방향을 바꿉니다.
2. 바라보고 있는 방향으로 이동하는 것이 가능한 경우
    1) 바로 앞이 격자 밖이라면 이동하여 탈출합니다.
    2) 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다면 그 방향으로 한 칸 이동합니다.
    3) 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 벽이 존재하지 않는다면,
       현재 방향으로 한 칸 이동 후 방향을 시계 방향으로 90' 만큼 방향을 틀어 한 칸 더 전진하여 오른쪽에 벽이 있게끔 합니다.

Input

첫째 줄에는 격자의 크기를 나타내는 양의 정수 N이 주어집니다.
둘째 줄에는 시작 위치 (x, y)가 주어집니다. x번째 행, y번째 열에서 시작함을 의미합니다. (1 ≤ x < N, 1 ≤ y ≤ N)
다음 N개의 줄에 걸쳐 각 행마다 미로의 모습을 나타내는 문자 N개가 공백없이 주어집니다.
해당 위치에 벽이 있는 경우에는 ‘#' 문자가, 벽이 없다면 '.’ 문자가 주어집니다.
시작 위치 (x, y)에는 벽이 절대 주어지지 않고, (x+1, y) 위치에는 항상 벽이 주어진다고 가정해도 좋습니다.

Output

방향을 트는 데에는 시간이 걸리지 않고 한 번 이동하는 데에는 1초의 시간이 걸린다고 했을 때,
미로를 탈출하는 데 걸리는 시간을 출력합니다.
오른쪽 벽을 짚고 따라가는 방식만으로 미로를 탈출하는 것이 불가능하다면 -1을 출력해주세요.

3
1 1
.#.
#..
...

1
--------------------------------
3
1 1
...
##.
...

7
--------------------------------
3
1 1
...
#..
...

5
--------------------------------
3
1 2
...
.#.
...

-1
"""

# my, 11%
import sys
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[0] * (n) for _ in range(n)]

x -= 1
y -= 1

dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 0
flag = True
while True:
    # 이동할 좌표
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 1:
        flag = False
        break
    else:
        visited[x][y] = 1
        # 이동할 좌표가 벽일 경우 반시계 방향으로 바꾸기만 하고 이동 x
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '#':
            dir = (dir + 3) % 4
            continue

        # 좌표 이동 및 횟수 카운팅
        count += 1
        x = x + dx[dir]
        y = y + dy[dir]

        # 이동한 좌표가 격자 밖이라면 반복문 탈출
        if x >= n or x < 0 or y >= n or y < 0:
            break

        # 이동한 좌표의 오른쪽에 벽이 없는 경우
        if board[x + dx[(dir + 1) % 4]][y + dy[(dir + 1) % 4]] == '.':
            # 시계 방향으로 90도 진행 방향 변경
            dir = (dir + 1) % 4

if flag:
    print(count)
else:
    print(-1)


# Sol
import sys

DIR_NUM = 4

# 변수 선언 및 입력
n = int(input())
curr_x, curr_y = tuple(map(int, input().split()))
a = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# 미로 탈출이 불가능한지 여부를 판단하기 위해
# 동일한 위치에 동일한 방향으로 진행했던 적이 있는지를
# 표시해주는 배열입니다.
visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n + 1)
    ]
    for _ in range(n + 1)
]
elapsed_time = 0

# 처음에는 우측 방향을 바라보고 시작합니다.
curr_dir = 0


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 위치에 벽이 있으면 이동이 불가합니다.
def wall_exist(x, y):
    return in_range(x, y) and a[x][y] == '#'


# 조건에 맞춰 움직여봅니다.
def simulate():
    global curr_x, curr_y, curr_dir, elapsed_time

    # 현재 위치에 같은 방향으로 진행한 적이 이미 있었는지 확인합니다.
    # 이미 한 번 겪었던 상황이라면, 탈출이 불가능 하다는 의미이므로
    # -1을 출력하고 프로그램을 종료합니다.
    if visited[curr_x][curr_y][curr_dir]:
        print(-1)
        sys.exit(0)

    # 현재 상황이 다시 반복되는지를 나중에 확인하기 위해
    # 현재 상황에 해당하는 곳에 visited 값을 True로 설정합니다.
    visited[curr_x][curr_y][curr_dir] = True

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    # Step1

    # 바라보고 있는 방향으로 이동하는 것이 불가능한 경우에는
    # 반 시계 방향으로 90' 방향을 바꿉니다.
    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir - 1 + 4) % 4

    # Step2

    # Case1
    # 바라보고 있는 방향으로 이동하는 것이 가능한 경우 중
    # 바로 앞이 격자 밖이라면 탈출합니다.
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elapsed_time += 1

    # Case 2 & Case 3
    # 바로 앞이 격자 안에서 이동할 수 있는 곳이라면
    else:
        # 그 방향으로 이동했다 가정헀을 때 바로 오른쪽에 짚을 벽이 있는지 봅니다.
        rx = next_x + dxs[(curr_dir + 1) % 4]
        ry = next_y + dys[(curr_dir + 1) % 4]

        # Case2
        # 그대로 이동해도 바로 오른쪽에 짚을 벽이 있다면
        # 해당 방향으로 한 칸 이동합니다.
        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elapsed_time += 1

        # Case3
        # 그렇지 않다면 2칸 이동후 방향을 시계방향으로 90' 방향을 바꿉니다.
        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir + 1) % 4
            elapsed_time += 2


for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start=1):
        a[i][j] = elem

# 격자를 빠져나오기 전까지 계속 반복합니다.
while in_range(curr_x, curr_y):
    # 조건에 맞춰 움직여봅니다.
    simulate()

print(elapsed_time)