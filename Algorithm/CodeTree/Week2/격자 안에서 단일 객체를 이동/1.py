"""
1 ~ 100 사이의 숫자로 이루어진 n * n 크기의 격자판 정보가 주어집니다.
이때 특정 위치에서 시작하여, 상하좌우로 인접한 곳에 있는 숫자들 중 현재 위치에 있는 숫자보다 더 큰 위치로 끊임없이 이동합니다.
만약 그러한 위치가 여러개 있는 경우, 상하좌우 방향 순서대로 우선순위를 매겨 가능한 곳 중 우선순위가 더 높은 곳으로 이동합니다.
격자를 벗어나서는 안되며, 더 이상 움직일 수 없을 때까지 반복합니다.

위의 규칙에 따라 방문하게 되는 위치에 적힌 숫자를 순서대로 출력하는 프로그램을 작성해보세요.

Input
4 2 2
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4

Output
5 8 11
"""
# My
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
x -= 1
y -= 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
answer.append(board[x][y])

while True:
    # 네 방향 모두 검사한지 체크할 변수
    count = 0
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나지 않고 현재 좌표의 수보다 큰 수일 경우
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]:
            # 좌표를 바꿔준 다음 바로 종료
            x = x + dx[i]
            y = y + dy[i]
            answer.append(board[x][y])
            break

        # 큰 수가 없다면 증가
        count += 1

    # 네 방향 모두 큰 수가 없으면 종료
    if count == 4:
        break

print(*answer)

# Sol
n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 방문하게 되는 숫자들을 담을 곳입니다.
visited_nums = []


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인합니다.
def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num


# 조건에 맞춰 움직여봅니다.
# 움직였다면 true를 반환하고
# 만약 움직일 수 있는 곳이 없었다면 false를 반환합니다.
def simulate():
    global curr_x, curr_y

    # 코딩의 간결함을 위해
    # 문제 조건에 맞게 상하좌우 순서로
    # 방향을 정의합니다.
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인합니다.
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        # 갈 수 있는 곳이라면
        # 이동하고 true를 반환합니다.
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y
            return True

    # 움직일 수 있는 곳이 없었다는 의미로
    # false 값을 반환합니다.
    return False


# 초기 위치에 적혀있는 값을 답에 넣어줍니다.
visited_nums.append(a[curr_x][curr_y])
while True:
    # 조건에 맞춰 움직여봅니다.
    greater_number_exist = simulate()

    # 인접한 곳에 더 큰 숫자가 없다면 종료합니다.
    if not greater_number_exist:
        break

    # 움직이고 난 후의 위치를 답에 넣어줍니다.
    visited_nums.append(a[curr_x][curr_y])

# 출력:
for num in visited_nums:
    print(num, end=' ')