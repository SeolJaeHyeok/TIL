import sys
from collections import deque
input = sys.stdin.readline

NOT_EXISTS = (-1, -1)

n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 위치
r, c = tuple(map(int, input().split()))
curr_cell = (r - 1, c - 1)

bfs_q = deque()
visited = [[0 for _ in range(n)] for _ in range(n)]


# 범위 내에 있는지 판단하는 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 해당 좌표로 이동이 가능한지 판별하는 함수
def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and \
           grid[x][y] < target_num


# visited 배열을 초기화
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


# 해당 좌표에서 도달 가능한 모든 좌표를 탐색하는 함수
def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    bfs_q.append(curr_cell)

    target_num = grid[curr_x][curr_y]

    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            if can_go(new_x, new_y, target_num):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True


# best 위치를 새로운 위치로 바꿔줘야 하는지를 판단하는 함수
def need_update(best_pos, new_pos):
    # 첫 도달 가능한 위치라면
    # update가 필요합니다.
    if best_pos == NOT_EXISTS:
        return True

    best_x, best_y = best_pos
    new_x, new_y = new_pos

    # 숫자, -행, -열 순으로 더 큰 곳이 골라져야 합니다.
    return (grid[new_x][new_y], -new_x, -new_y) > \
           (grid[best_x][best_y], -best_x, -best_y)


# 가장 우선순위가 높은 위치를 찾아
# 위치를 이동합니다.
def move():
    global curr_cell # 현재 위치

    # BFS 탐색을 위한 초기화 작업을 수행합니다.
    initialize_visited()

    # Step1. BFS를 진행하여 갈 수 있는 모든 위치를 탐색합니다.
    bfs()

    # Step2.
    # 도달 할 수 있는 위치들 중
    # 가장 우선순위가 높은 위치를 구합니다.
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            # 도달이 불가능하거나 현재 위치는 건너뜁니다.
            if not visited[i][j] or (i, j) == curr_cell:
                continue

            # 새로운 위치를 초기화 하고
            new_pos = (i, j)
            # 그 위치로 변경이 되어야 하는지 판단
            if need_update(best_pos, new_pos):
                best_pos = new_pos

    # Step3. 위치를 이동합니다.

    # 만약 움직일 위치가 없다면 종료합니다.
    if best_pos == NOT_EXISTS:
        return False
    # 움직일 위치가 있다면 이동합니다.
    else:
        curr_cell = best_pos
        return True


# k번에 걸쳐 움직이는 것을 반복합니다.
for _ in range(k):
    is_moved = move()

    # 움직이지 못했다면 바로 종료합니다.
    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)