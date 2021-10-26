# DFS 기본 구조
def recursive_dfs(v, discovered=[]):
    # 방문 리스트(정답)에 추가하고
    discovered.append(v)
    # 해당 정점에 연결된 정점을 순서대로 탐색
    for w in graph[v]:
        # 방문하지 않은 정점이라면
        if w not in discovered:
            # 해당 정점을 기준으로 재귀 호출
            recursive_dfs(w, discovered)
    return discovered

def iterate_dfs(vertex):
    discovered = []
    # 시작 정점을 스택에 추가하고
    stack = [vertex]
    # 스택이 빌 때까지 반복
    while stack:
        # 스택에서 꺼낸 후
        v = stack.pop()
        # 해당 정점이 방문하지 않은 정점이라면
        if v not in discovered:
            # 방문 처리(정답 리스트에 추가)
            discovered.append(v)
            # 그런 다음 해당 정점과 연결된 정점들 스택에 추가
            for w in graph[v]:
                stack.append(w)

    return discovered

def recursive_dfs2(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for w in graph[v]:
        if not visited[w]:
            recursive_dfs2(graph, w, visited)


graph = {
    0: [],
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
visited = [False] * len(graph)

print(recursive_dfs(1))
print(iterate_dfs(1))
recursive_dfs2(graph, 1, visited)
"""
BackTracking
- 백트래킹은 DFS와 유사하지만 좀 더 광의의 의미를 가진다.
- 백트래킹은 탐색을 하다가 더이상 갈 수 없으면 되돌아가 다른 길을 찾는 방식, 주로 재귀로 구현
"""