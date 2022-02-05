import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

array = [[] * m for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)
    array[a].sort()
    array[b].sort()

def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for next_node in array[start]:
        if not visited[next_node]:
            dfs(next_node)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for next_node in array[x]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True

for i in range(2):
    visited = [False] * (n + 1)
    if i == 0:
        dfs(v)
    else:
        bfs(v)
    print()