import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((s[0], s[1]))
    while q:
        x, y = q.popleft()
        # 이동한 좌표가 목적지까지 도달할 수 있다면 True
        if abs(x - e[0]) + abs(y - e[1]) <= 1000:
            return True
        # 편의점의 수만큼 반복
        for i in range(n):
            nx, ny = m[i] # 편의점 좌표
            # 방문하지 않은 편의점이면서 편의점까지 이동이 가능한 경우
            if not visited[i] and abs(x - nx) + abs(y - ny) <= 1000:
                q.append((nx, ny))
                visited[i] = 1

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split())) # 시작 좌표
    m = [] # 편의점 좌표
    for _ in range(n):
        m.append(list(map(int, input().split())))
    e = list(map(int, input().split())) # 목적지 좌표
    visited = [0 for i in range(n + 1)]
    
    if bfs():
        print('happy')
    else:
        print('sad')
