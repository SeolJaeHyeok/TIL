import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
subtree = [0] * (n + 1) # 각 정점이 가진 서브트리의 수

# 양방향 그래프 구성
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

rootNodes = [int(input()) for _ in range(q)]
visited = [False] * (n + 1)

def dfs(currentNode):
    # 현재 노드를 루트노드로 하는 서브트리가 하나 존재하기 때문에 1로 시작
    subtree[currentNode] = 1
    visited[currentNode] = True
    for nextNode in graph[currentNode]:
        if not visited[nextNode]:
            dfs(nextNode)
            subtree[currentNode] += subtree[nextNode]
            # print(subtree)

# 루트 노드를 정점으로 DFS 탐색
dfs(r)

for root in rootNodes:
    print(subtree[root])