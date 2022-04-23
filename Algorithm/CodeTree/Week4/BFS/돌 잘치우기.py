# 1, combinations 메소드를 통해 모든 경우의 수 구하기
import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n, k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
start_pos = [list(map(int, input().split())) for _ in range(k)]

# 기본 BFS 탐색
def bfs(i, j):
    global count
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 방문하지 않았고 0인 경우 방문처리, 카운팅, 큐에 추가
            if not visited[nx][ny] and a[nx][ny] == 0:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))


# 1이 적힌 모든 좌표
all_pos = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            all_pos.append((i, j))

# 1이 적힌 좌표 중 m개만큼 없애는 모든 경우의 수
comb = list(combinations(all_pos, m))

answer = 0

for com in comb:
    # 입력받은 board 깊은 복사
    # 이렇게 하지 않으면 m개의 좌표를 치우는 과정이 계속해서 누적되므로
    # 항상 시작 배열에서 m개를 빼줘야 한다.
    # 따라서 모든 경우를 탐색할 때 원본 배열을 복사하여 이 배열을 가지고 탐색을 진행
    a = copy.deepcopy(board)

    # m개의 좌표 치우기
    for co in com:
        x, y = co
        a[x][y] = 0

    # 입력 받은 모든 시작 좌표로부터 탐색 시작
    for start in start_pos:
        r, c = start
        r -= 1
        c -= 1

        visited = [[False] * n for _ in range(n)]

        # 시작 좌표 포함하므로 1부터 시작
        count = 1

        # 탐색 시작
        bfs(r, c)
        # 탐색후 이동 가능한 좌표의 횟수의 최대값 갱신
        answer = max(answer, count)

print(answer)

# 2, backtracking을 통해 모든 경우의 수 구하기
from collections import deque

# 변수 선언 및 입력
n, k, m = tuple(map(int, input().split()))
a = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
s_pos = []
stone_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if a[i][j] == 1
]
selected_stones = []

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    return in_range(x, y) and not a[x][y] and not visited[x][y]


def bfs():
    # queue에 남은 것이 없을때까지 반복합니다.
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()

        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

        # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부를 표시해줍니다.
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True


def calc():
    # 돌 치우기
    for x, y in selected_stones:
        a[x][y] = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # k개의 시작점을 queue에 넣고 시작합니다.
    # BFS는 여러 시작점에서 시작하여
    # 이동 가능한 칸을 전부 탐색하는 것이 가능합니다.
    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True

    bfs()

    # 탐색 후 다시 채워주기
    for x, y in selected_stones:
        a[x][y] = 1

    # 방문한 좌표 개수 카운팅
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt


def find_max(idx, cnt):
    global ans

    if idx == len(stone_pos):
        if cnt == m:
            ans = max(ans, calc())
        return

    selected_stones.append(stone_pos[idx])
    find_max(idx + 1, cnt + 1)
    selected_stones.pop()

    find_max(idx + 1, cnt)


for _ in range(k):
    r, c = tuple(map(int, input().split()))
    s_pos.append((r - 1, c - 1))

find_max(0, 0)
print(ans)