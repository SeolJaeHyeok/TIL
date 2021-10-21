from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque()
q.append(x)

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

for i in range(1, n + 1):
    if k == distance[i]:
        print(i)

if k not in distance:
    print(-1)




