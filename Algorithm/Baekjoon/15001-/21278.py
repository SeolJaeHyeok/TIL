import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 와샬 알고리즘
for k in range(1, n + 1):
    graph[k][k] = 0 # 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


answer = []
time = 1e9
for i in range(1, n + 1):
    for j in range(1, n + 1):
        tmp = 0 # 치킨집까지 편도 시간
        # 편도 시간의 최소값을 구하고
        for k in range(1, n + 1):
            tmp += min(graph[k][i], graph[k][j])

        # i와 j에 치킨집을 세웠을 때 걸리는 왕복 시간이 더 작을 경우 값 갱신
        if time > tmp * 2:
            time = tmp * 2
            answer = [i, j, time]

print(*answer)
