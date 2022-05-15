import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드에 대한 정보(거리과 현재 노드) 꺼내기
        dist, now = heapq.heappop(q)

        # 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드 확인
        for next_node in board[now]:
            # 해당 노드까지 가는 비용 계산
            # 현재 노드까지의 거리 + 해당 노드로 이동하는데 필요한 거리
            cost = dist + next_node[1]

            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 값 갱신하고 큐에 추가
            if cost < distance[next_node[0]]:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))


n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    board[a].append((b, c)) # a에서 b로 가는 비용이 c
    board[b].append((a, c)) # b에서 a로 가는 비용이 c

dijkstra(1)

# n번 헛간까지의 최단거리
print(distance[-1])