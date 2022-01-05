# 1, 간단한 다익스트라 -> 시간 초과, 매번 최단 거리가 가장 짧은 노드를 선형 탐색
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for i in range(n + 1)]

# 간선 정보 입력
for i in range(m):
    start, end, time = map(int, input().split())
    # start 마을에서 end 마을까지 걸리는 시간이 time
    graph[start].append((end, time))

def get_smallest_node(distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node(distance, visited)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

    return distance

answer = 0
for i in range(1, n + 1):
    s = dijkstra(i)
    e = dijkstra(x)
    answer = max(answer, s[x] + e[i])

print(answer)


# 2, 개선된 다익스트라 -> 힙 자료구조를 이용하여 속도 개선
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for i in range(n + 1)]

# 간선 정보 입력
for i in range(m):
    start, end, time = map(int, input().split())
    # start 마을에서 end 마을까지 걸리는 시간이 time
    graph[start].append((end, time))


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 값을 갱신하고 큐에 추가
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

answer = 0
for i in range(1, n + 1):
    s = dijkstra(i) # 각 출발 노드에서 갈 수 있는 노드들에 대한 최단거리
    e = dijkstra(x) # x번 마을에서 다른 마을들로 가는 최단 거리
    # x번 마을을 제외한 각 마을에서 x번 마을로 가는 최단 거리 + x번 마을에서 각 마을로 가는 최단거리를 더하여
    # 가장 큰 값이 최단 거리로 이동하는 학생들 중 가장 많은 시간을 소비하는 학생이 된다.
    answer = max(answer, s[x] + e[i])

print(answer)


