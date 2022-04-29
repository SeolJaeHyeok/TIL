"""
N*M 크기의 격자로 구성된 마을이 있습니다. 격자마다 한 집을 의미하며, 각 집의 높이는 1에서 100 사이의 숫자로 이루어져 있습니다.

이런 상황에서 만약 비가 K (K >= 1)만큼 온다고 한다면,
마을에 있는 집들 중 높이가 K 이하인 집들은 전부 물에 잠기게 되기 때문에,
대책을 세우기 위해 미리 각 K에 따라 안전 영역의 개수가 어떻게 달라지는지를 보려고 합니다.

여기서 안전 영역이란 잠기지 않은 집들로 이루어져 있으며, 잠기지 않은 집들끼리 서로 인접해 있는 경우 동일한 안전 영역에 있는 것으로 봅니다.

이런 상황에서 안전 영역의 수가 최대가 될때의 K와 그때의 안전 영역의 수를 구해주는 프로그램을 작성해보세요.

Input

4 5                 3 2
1 2 4 7 5           1 2
4 2 5 5 2           2 2
5 7 3 2 6           1 1
6 7 4 5 1

Output

4 4                 1 1
"""

# My
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
answer = []

# 마을에서 가장 큰 k 값 찾기
max_k = 0
for b in board:
    max_k = max(max_k, max(b))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 비에 잠기는 구역을 만드는 함수
def process1(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if board[nx][ny] <= k:
                process1(nx, ny)
                visited[nx][ny] = 1


# 비에 잠기지 않은 구역의 영역의 수를 찾는 함수
def process2(x, y):
    # 범위를 벗어나면 그대로 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    # 잠기지 않은 마을인 경우
    if visited[x][y] == 0:
        # 방문 처리하고
        visited[x][y] = 2

        # 상, 하, 좌, 우 탐색
        process2(x + 1, y)
        process2(x - 1, y)
        process2(x, y + 1)
        process2(x, y - 1)
        return

    return


k = 1
while k <= max_k:
    visited = [[0] * m for _ in range(n)]
    safe_area = 0

    # k보다 작은 마을을 기준으로 비에 잠기게 만들기
    for i in range(n):
        for j in range(m):
            if board[i][j] <= k:
                process1(i, j)
            else:
                continue

    # 비에 잠긴 후 남은 영역(visited가 0인 마을)들 중 안전영역의 수 구하기
    for i in range(n):
        for j in range(m):
            # 잠기지 않은 마을인 경우
            if not visited[i][j]:
                # 그 마을을 기준으로 상,하,좌,우 잠기지 않은 영역 확장
                process2(i, j)
                # 그 후 안전영역 증가
                safe_area += 1

    answer.append((k, safe_area))

    k += 1

answer.sort(key=lambda x: x[1], reverse=True)
print(*answer[0])

# Sol
import sys

sys.setrecursionlimit(2500)

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

zone_num = 0


# visited 배열을 초기화해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(x, y, k):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] <= k:
        return False

    return True


def dfs(x, y, k):
    # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # 네 방향에 각각에 대하여 DFS 탐색을 합니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y, k):
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)


def get_zone_num(k):
    global zone_num

    # 새로운 탐색을 시작한다는 의미로 zone_num를 0으로 갱신하고
    # visited 배열을 초기화해줍니다.
    zone_num = 0
    initialize_visited()

    # 격자의 각 위치에 대하여 탐색을 시작할 수 있는 경우
    # 해당 위치로부터 시작한 DFS 탐색을 수행합니다.
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                # 해당 위치를 탐색할 수 있는 경우 visited 배열을 갱신하고
                # 안전 영역을 하나 추가해줍니다.
                visited[i][j] = True
                zone_num += 1

                dfs(i, j, k)


# 가능한 안전 영역의 최솟값이 0이므로 다음과 같이 초기화 해줄 수 있습니다.
max_zone_num = -1
answer_k = 0
max_height = 100

# 각 가능한 비의 높이에 대하여 안전 영역의 수를 탐색합니다.
for k in range(1, max_height + 1):
    get_zone_num(k)

    # 기존의 최대 영역의 수보다 클 경우 이를 갱신하고 인덱스를 저장합니다.
    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)