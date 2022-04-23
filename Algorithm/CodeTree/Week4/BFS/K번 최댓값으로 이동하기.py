"""
n*n 크기의 격자에 1에 100 사이의 숫자가 각 칸에 하나씩 주어져 있습니다.
이때 특정 위치에서 시작하여 아래 조건을 만족하는 숫자의 위치를 찾아 상하좌우로만 이동합니다.
이렇게 이동하는 것을 k번 반복한 이후의 위치를 구하는 프로그램을 작성해보세요.
만약 아직 k번을 반복하지 못했지만, 더 이상 새로 이동할 위치가 없다면 움직이는 것을 종료합니다.

한번 이동하기 위한 조건은 다음과 같습니다.

Ex)
    1   3   2   11
    4   9   6   9
    2   6   9   8
    1   9   10  7

1. 시작 위치에 적혀있는 숫자를 x라고 했을 때, 시작 위치에서 출발하여 인접한 칸들 중 적혀있는 숫자가 x보다 작은 곳으로는 전부 이동이 가능합니다
위 행렬을 예로 들어보면, 시작 위치가 4행 3열인 숫자 10이라고 했을 때, 10보다 큰 11을 제외한 인접한 모든 숫자들로 이동이 가능합니다.
    1-1. 하지만 만약에 아래 그림처럼 시작 위치의 상하좌우가 시작 숫자(= 10)보다 큰 숫자들(= 11)로 둘러쌓여져 있으면 이동이 불가합니다.

2. 1번 조건을 만족하며 도달할 수 있는 칸들에 적혀있는 숫자 중 최댓값으로 이동합니다.
위 행렬과 같이 시작 위치에 적혀있는 숫자 10에서 출발하여 인접한 칸들 중 10보다 작지만 그 중 최댓값인 (모든)9로 이동을 고려합니다.

3. 2번 조건을 만족하는 숫자가 여러개 일경우, 행 번호가 가장 작은 곳으로 이동합니다.
아래 행렬과 같이 2행에 있는 최댓값(= 9)이 두개 있습니다.

    1   3   2   11
    4   9   6   9
    2   6   9   8
    1   9   10  7

4. 2번 조건을 만족하고, 행 번호도 같은 숫자가 여러개 일경우, 열 번호가 가장 작은 곳으로 이동합니다.

-----------------------------------------------------------------------------

결론적으로 4행 3열에서 시작하여 인접한 곳으로 숫자 10보다 작은 곳들로 이동했을 때 갈 수 있는 칸들 중 최대 숫자는 9이고,
그 중 우선순위가 가장 높은 곳은 2행 2열입니다. 따라서 2행 2열 위치로 이동하게 됩니다.

2행 2열 위치를 시작으로 한번 더 움직임을 반복해보면,
2행 2열에서 시작하여 인접한 곳으로 숫자 9보다 작은 곳들로 이동했을 때 갈 수 있는 칸들 중 최대 숫자는 6이고,
그 중 우선순위가 가장 높은 곳은 2행 3열입니다. 따라서 2행 3열 위치로 이동하게 됩니다.

2행 3열 위치를 시작으로 한번 더 움직임을 반복해보면,
2행 3열에서 시작하여 인접한 곳으로 숫자 6보다 작은 곳들로 이동했을 때 갈 수 있는 칸들 중 최대 숫자는 4이고, 4는 2행 1열입니다.
따라서 2행 1열 위치로 이동하게 됩니다.

이렇게 이동하는 것을 k번 반복한 후의 위치를 구하는 프로그램을 작성해보세요.
아직 k번을 반복하지 못했더라도, 더 이상 새로 이동할 위치가 없다면 움직이는 것을 종료해야함에 유의합니다.


Input
4 3             4 4
4 2             1 3 2 11
1 3 2 11        4 9 6 9
4 9 6 9         2 6 9 8
2 6 9 8         1 9 10 7
1 9 10 7        4 3
4 3

Output
2 3             1 2
"""
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