# bfs 기본 구조
# bfs는 재귀로 구현 불가
from collections import deque

def bfs(start_v):
    discovered = [start_v]
    q = deque([start_v])
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in discovered:
                q.append(w)
                discovered.append(w)
    return discovered


graph = {
    0: [],
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

print(bfs(1))
