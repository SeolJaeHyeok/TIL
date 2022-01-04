import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        # 큐에서 하나를 뽑은 뒤
        x = q.popleft()
        # 해당 원소와 연결되어 있고 아직 방문하지 않은 노드들을 방문 후 큐에 삽입
        for next_node in graph[x]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
                # 해당 원소의 값에 1을 더하여 연결된 노드의 값(촌수) 갱신
                answer[next_node] = answer[x] + 1

n = int(input())
a, b = map(int, input().split())
m = int(input())

# 부모-자식 관계 양방향 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 촌수 계산 결과를 저장할 리스트와 방문 처리를 위한 리스트 선언
answer = [0 for i in range(n + 1)]
visited = [False] * (n + 1)

# 탐색한 후 조건에 맞게 출력
bfs(a)
print(answer[b] if answer[b] else '-1')