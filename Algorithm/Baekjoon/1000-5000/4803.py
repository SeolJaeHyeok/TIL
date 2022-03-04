import sys
from collections import deque
input = sys.stdin.readline

# 1, 16%
def dfs(start):
    visited[start] = True
    if len(graph[start]) == 1 or len(graph[start]) == 0:
        return True

    for next_node in graph[start]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

    return False


flag = 0
while True:
    flag += 1
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    if n == 0 and m == 0:
        break

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)

    count = -1
    for i in range(1, n + 1):
        if dfs(i):
            count += 1

    if count > 1:
        print(f'Case {flag}: A forest of {count} trees.')
    elif count == 1:
        print(f'Case {flag}: There is one tree.')
    else:
        print(f'Case {flag}: No trees.')

# 2, sol
def bfs(start):
    q = deque()
    q.append(start)
    flag = True
    while q:
        cur = q.popleft()
        # 현재 노드가 이전에 방문했던 노드라면 사이클
        if visited[cur]:
            flag = False

        # 사이클이 아닐 경우 방문 처리
        visited[cur] = True

        # 연결된 노드의 방문 여부에 따라 큐에 추가
        for next_node in graph[cur]:
            if not visited[next_node]:
                q.append(next_node)

    return flag

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    if n == 0 and m == 0:
        break

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    answer = 0
    for i in range(1, n + 1):
        if bfs(i):
            answer += 1

    if answer > 1:
        print(f'Case {case}: A forest of {answer} trees.')
    elif answer == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
