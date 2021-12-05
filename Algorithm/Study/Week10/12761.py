# 1
from collections import deque
import sys

def bfs(node):
    q = deque()
    q.append(node)
    graph[node] = 0
    while q:
        node = q.popleft()
        for n in [node-1, node+1, node+A, node-A, node+B, node-B, node*A, node*B]:
            if (0 <= n <= 100000) and graph[n] == -1:
                q.append(n)
                graph[n] = graph[node]+1
                if n == M:
                    return ;

A, B, N, M = map(int, input().split())
graph = [-1]*100001
bfs(N)
print(graph[M])

# 2
input = sys.stdin.readline
def bfs():
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x + d[i]
                if 0 <= nx <= 100000 and visit[nx] == 0:
                    q.append(nx)
                    visit[nx] = 1
                    s[nx] = s[x] + 1
            else:
                nx = x * d[i]
                if 0 <= nx <= 100000 and visit[nx] == 0:
                    q.append(nx)
                    visit[nx] = 1
                    s[nx] = s[x] + 1
a, b, n, m = map(int, input().split())
s = [0 for i in range(100001)]
visit = [0 for i in range(100001)]
visit[n] = 1
d = [1, -1, a, -a, b, -b, a, b]
q = deque()
q.append(n)
bfs()
print(s[m])

