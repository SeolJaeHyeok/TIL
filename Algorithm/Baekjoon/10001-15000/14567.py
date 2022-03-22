import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
time = [0] * (n + 1)

array = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b) # 노드 A에서 B로 이동 가능
    indegree[b] += 1 # 진입 차수 1 증가

q = deque()
for i in range(1, n + 1):
    # 진입 차수가 0인 경우 큐에 추가
    if indegree[i] == 0:
        q.append(i)
        time[i] = 1 # 진입 차수가 0이면 1학기에 이수 가능

while q:
    node = q.popleft() # 선수 과목
    for i in array[node]:
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        indegree[i] -= 1
        # 선수 과목을 모두 들은 후 해당 과목을 이수했을 경우로 갱신
        # time[i] = 현재 과목을 듣기 전까지의 수강한 학기 + 현재 학기
        time[i] = time[node] + 1
        # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

print(*time[1:])