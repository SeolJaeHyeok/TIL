# Small World Network
# DFS, 예외 처리가 완벽하게 이뤄지지 않음
import sys
n, k = map(int, sys.stdin.readline().split())

array = [[] for i in range(n + 1)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    array[b].append(a)

def dfs(idx, visited):
    visited[idx] = 1
    for i in array[idx]:
        if not visited[i]:
            dfs(i, visited)

visited = [0] * (n + 1)
check = True
for i in range(1, n + 1):
    dfs(i, visited)
    # print(visited)
    if sum(visited) < n or 0 in visited[1:]:
        check = False
        break

if check:
    print('Small World!')
else:
    print('Big World!')


# BFS
from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 0
    while q:
        node = q.popleft()
        for next_node in array[node]:
            if visited[next_node] == -1:
                q.append(next_node)
                visited[next_node] = visited[node] + 1


n, k = map(int, input().split())
array = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

check = True
for i in range(1, n + 1):
    visited = [-1] * (n + 1)
    bfs(i)
    if (max(visited) > 6) or (-1 in visited[1:]):
        check = False
        break

print("Small World!" if check else "Big World!")
