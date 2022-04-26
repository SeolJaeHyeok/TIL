import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, target = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0] * (n + 1) # start를 기준으로 각 숫자의 촌수를 저장할 배열
visited = [False] * (n + 1)

def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        now = q.popleft() # 현재 노드
        # 현재 노드와 연결된 다른 노드 탐색
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                answer[next_node] = answer[now] + 1 # 현재에 노드와 연결된 노드들은 이전까지의 촌수 + 1
                q.append(next_node)

# 둘 중 한 쪽으로 탐색 시작
bfs(start)

# target이 start와 연결이 되어있으면 해당 촌수 출력
if answer[target]:
    print(answer[target])
else:
    print(-1)