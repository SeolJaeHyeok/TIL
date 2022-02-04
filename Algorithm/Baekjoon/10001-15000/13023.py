import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

n, m = map(int, input().split())

# 양방향 그래프 입력받기
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, num):
    global answer
    # 노드의 깊이가 5라면 1 출력 후 종료
    if num == 4:
        print(1)
        exit()
    # 노드의 깊이를 하나씩 늘려가면 재귀 탐색
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, num + 1)
            visited[i] = False

# 방문 처리 리스트
visited = [False] * n
for i in range(n):
    # 시작 노드 방문처리
    visited[i] = True
    dfs(i, 0)
    # 탐색이 끝난 후 새로운 노드를 시작노드로 탐색할 때는 모든 노드의 방문 상태가 False가 되어야하므로 False 할당
    visited[i] = False

# 노드의 깊이 조건이 만족하지 않은 경우 0 출력
print(0)
