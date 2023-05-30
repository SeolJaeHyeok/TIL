from collections import deque

def bfs(graph, start, visited):
    # 방문한 노드를 저장할 큐를 생성합니다.
    queue = deque([start])
    # 현재 영역의 크기를 저장하는 변수를 초기화합니다.
    size = 0

    # 큐가 빌 때까지 반복합니다.
    while queue:
        # 큐에서 노드를 꺼냅니다.
        node = queue.popleft()
        if node not in visited:
            # 방문하지 않은 노드라면 방문 처리하고 인접 노드를 큐에 추가합니다.
            visited.append(node)
            size += 1
            for i in range(len(graph[node])):
                if graph[node][i] == 1 and i not in visited:
                    queue.append(i)

    return size

def count_areas(arr):
    # 그래프를 생성합니다.
    graph = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                node = i * len(arr[0]) + j
                if node not in graph:
                    graph[node] = []
                # 인접 노드를 그래프에 추가합니다.
                if i > 0 and arr[i-1][j] == 1:
                    graph[node].append((i-1) * len(arr[0]) + j)
                if i < len(arr)-1 and arr[i+1][j] == 1:
                    graph[node].append((i+1) * len(arr[0]) + j)
                if j > 0 and arr[i][j-1] == 1:
                    graph[node].append(i * len(arr[0]) + j-1)
                if j < len(arr[0])-1 and arr[i][j+1] == 1:
                    graph[node].append(i * len(arr[0]) + j+1)

    # BFS 탐색으로 영역의 크기와 개수를 구합니다.
    visited = []
    areas = []
    for node in graph:
        if node not in visited:
            size = bfs(graph, node, visited)
            areas.append(size)

    return len(areas), areas


print(count_areas([[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1]]))