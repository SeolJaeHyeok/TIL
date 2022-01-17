import sys
from collections import deque
input = sys.stdin.readline

def check(x, y):
    if not visited[x][y]:
        q.append((x, y))
        visited[x][y] = True

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y
        # a 물통이 비어있을 경우 답 저장
        if x == 0:
            answer.append(z)

        # 6가지의 이동 가능한 경우 모두 탐색
        # a물통 -> b물통
        moving_water = min(x, b - y)  # 움직이는 물의 양, 전체 다 옮기는 경우와 두 물통의 차이만큼 옮기는 경우 중 작은 경우의 물의 양
        check(x - moving_water, y + moving_water)
        # a물통 -> c물통
        moving_water = min(x, c - z)
        check(x - moving_water, y)
        # b물통 -> a물통
        moving_water = min(y, a - x)
        check(x + moving_water, y - moving_water)
        # b물통 -> c물통
        moving_water = min(y, c - z)
        check(x, y - moving_water)
        # c물통 -> a물통
        moving_water = min(z, a - x)
        check(x + moving_water, y)
        # c물통 -> b물통
        moving_water = min(z, b - y)
        check(x, y + moving_water)


a, b, c = map(int, input().split())
visited = [[False] * (b + 1) for _ in range(a + 1)] # 모든 경우의 수 방문처리를 위한 리스트
answer = []

q = deque()
q.append((0, 0))        # a와 b물통 모두 0인 상태로 시작
visited[0][0] = True    # (0, 0) 방문처리

bfs()

for i in sorted(answer):
    print(i, end=' ')
