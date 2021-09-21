# 전보
# my
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
total = 0
for d in distance:
    if d != 1e9:
        count += 1
        total = max(total, d)

print(count - 1, total)
# sol
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 Z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
   q = []
   # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
   heapq.heappush(q, (0, start))
   distance[start] = 0
   while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)


"""
접근 방법
한 도시에서 다른 도시로 전보를 보낼 수 있는 경우이므로 최단 거리 알고리즘을 이용해서 풀어야 하고 입력값의 범위가 충분히 크기 때문에
우선 순위 큐를 이용한 다익스트라 알고리즘을 적용해서 풀이

- 입력값을 입력 받고 학습한 다익스트라 알고리즘을 동일하게 적용
- 우선 순위 큐를 이용한 다익스트라 알고리즘이기 때문에 큐에 추가할 때는 간선의 비용이 적은(전보를 보내는데 적은 시간이 걸리는) 순서대로 정렬이 된다.
- 그런 다음 메세지를 받은 도시의 수와 메세지를 받는 시간을 처리하는데 도시의 수는 초기에 무한의 값으로 초기화한 최단 거리 테이블이 무한의 값이 아닌 경우
전보가 전달된 것이고 자기 자신은 포함하면 안되므로 -1을 해준다. 그리고 메세지는 동시에 전달이 될 것이므로 무한의 값이 아닌 최단 거리 테이블 중 가장 큰 값을 출력 
"""