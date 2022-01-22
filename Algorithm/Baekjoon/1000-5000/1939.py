import sys
from collections import deque
input = sys.stdin.readline

def bfs(mid):
    visited[start] = True
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        # 목적지까지 도달했을 경우 True
        if now == end:
            return True
        # 현재 다리(now)와 연결된 다리(bName)와 건너갈 수 있는 무게(weight)
        for bName, weight in graph[now]:
            # 연결된 다리가 방문한 적이 없고 건너갈 수 있는 경우
            if visited[bName] == 0 and mid <= weight:
                # 큐에 추가 후 방문 처리
                q.append(bName)
                visited[bName] = True

    # 목적지까지 도달하지 못했을 경우 False
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 다리 정보 입력받기 - 양방향
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

# 내림차순 정렬
for i in range(1, n + 1):
    graph[i].sort(reverse=True)

start, end = map(int, input().split())
left, right = 1, 1000000000
while left <= right:
    visited = [False] * (n + 1)
    mid = (left + right) // 2
    if bfs(mid): # 목적지 까지 도달 가능한 경우
        # 시작값 늘리기
        left = mid + 1
    else: # 목적지까지 도달 불가능한 경우
        # 끝값 줄이기
        right = mid - 1

print(right)