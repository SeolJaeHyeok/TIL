# My
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 폭탄이 터지는 횟수
bomb_count = 0
for b in board:
    bomb_count += b.count(1)

dir_mapper = {
    1: [[1, 2, -1, -2], [0, 0, 0, 0]],
    2: [[1, 0, -1, 0], [0, 1, 0, -1]],
    3: [[-1, -1, 1, 1], [-1, 1, -1, 1]]
}


def explode(nums, visited):
    for num in nums:
        dx, dy = dir_mapper[num]
        for x in range(n):
            for y in range(n):
                if board[x][y] == 1:
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                            continue

                        visited[nx][ny] = True
    for k in visited:
        print(*k)
    print()
    return


nums = []


def Choose(cnt):
    if cnt == bomb_count + 1:
        visited = [[False] * n for _ in range(n)]
        a = [[0] * n for _ in range(n)]
        # print(nums)
        explode(nums, visited)
        return

    for i in range(1, 4):
        nums.append(i)
        Choose(cnt + 1)
        nums.pop()


Choose(1)

for b in board:
    print(*b)


# Sol 1
n = int(input())
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
bombed = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0

bomb_pos = list()


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def bomb(x, y, b_type):
    # 폭탄 종류마다 터질 위치를 미리 정의합니다.
    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]

    # 격자 내 칸에 대해서만 영역을 표시합니다.
    for i in range(5):
        dx, dy = bomb_shapes[b_type][i];
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bombed[nx][ny] = True


def calc():
    # Step1. 폭탄이 터진 위치를 표시하는 배열을
    # 초기화합니다.
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False

    # Step2. 각 폭탄의 타입에 따라
    # 초토화 되는 영역을 표시합니다.
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])

    # Step3. 초토화된 영역의 수를 구합니다.
    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1

    return cnt


def find_max_area(cnt):
    global ans

    if cnt == len(bomb_pos):
        ans = max(ans, calc())
        return

    for i in range(1, 4):
        x, y = bomb_pos[cnt]

        bomb_type[x][y] = i
        find_max_area(cnt + 1)
        bomb_type[x][y] = 0


for i in range(n):
    given_row = list(map(int, input().split()))
    for j, bomb_place in enumerate(given_row):
        if bomb_place:
            bomb_pos.append((i, j))

find_max_area(0)

print(ans)

# Sol2
from copy import deepcopy

def explode_and_count(board):
    global _max

    visited = [[False] * N for _ in range(N)]
    tot = len(booms)

    for cx,cy in booms: # 폭탄 위치 일단 체크
        visited[cx][cy] = True

    for sx,sy in booms: # 폭탄 위치 꺼내오기
        lst = dics[data[sx][sy]] # 해당 폭탄 위치 이동해야 하는 현재 +- 위치들ㅑ

        for x,y in lst:
            nx, ny = sx + x, sy + y

            if 0 <= nx < N and 0 <= ny <N and not visited[nx][ny]:
                visited[nx][ny] = True
                tot += 1
    _max = max(tot, _max)

def write_boom():  # booms -> 폭탄 위치, match_pos -> lst 속에 1,2,2 이런식의 폭탄이 들어있음
    for idx in range(len(booms)):
        x, y = booms[idx]
        data[x][y] = match_pos[idx]

    explode_and_count(deepcopy(data))

def back(cur_num):
    global boom_size

    if cur_num == boom_size + 1:
        write_boom()
        return

    for a in range(1, 4):
        match_pos.append(a)
        back(cur_num + 1)
        match_pos.pop()


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
_max = 0
match_pos = []
booms = []
dics = {1: [(-1, 0), (-2, 0), (1, 0), (2, 0)], 2: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        3: [(-1, -1), (-1, 1), (1, -1), (1, 1)]}

for i in range(N):  # 폭탄 위치 찾기
    for j in range(N):
        if data[i][j] != 0:
            booms.append((i, j))
            data[i][j] = 0

boom_size = len(booms)

back(1)
print(_max)