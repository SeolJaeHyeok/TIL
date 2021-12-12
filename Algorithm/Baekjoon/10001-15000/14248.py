# 점프 점프
# bfs로 탐색
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1 # 시작 노드 방문 처리
    while q:
        now = q.popleft()
        # 왼쪽 오른쪽으로 점프 하는 두 개의 경우
        for i in [-array[now], array[now]]:
            next_node = now + i  # 양 쪽으로 점프한 노드
            # 점프한 노드가 범위를 벗어나지 않고 방문한 적이 없다면
            if 0 <= next_node < n and visited[next_node] == -1:
                # 큐에 추가 후 방문 처리
                q.append(next_node)
                visited[next_node] = 1


n = int(input())
array = list(map(int, input().split()))
s = int(input()) - 1
visited = [-1] * n

bfs(s)
print(visited.count(1))



