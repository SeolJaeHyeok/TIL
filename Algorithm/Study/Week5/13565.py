# 침투
# dfs 탐색
def dfs(graph, visited, x, y):
    # 종료 조건
    if x >= m or x < 0 or y >= n or y < 0 or visited[x][y] == 1 or graph[x][y] == 1:
        return False

    # 방문 처리
    visited[x][y] = 1
    # 재방문을 방지하기 위해 지나온 곳 처리
    graph[x][y] = 1

    # 동,서,남,북으로 탐색
    dfs(graph, visited, x + 1, y)
    dfs(graph, visited, x - 1, y)
    dfs(graph, visited, x, y + 1)
    dfs(graph, visited, x, y - 1)

    return True

m, n = map(int, input().split())
graph = []
# 격자 입력 받기
for _ in range(m):
    graph.append(list(map(int, input())))
# 방문처리를 위한 리스트
visited = [[0] * n for _ in range(m)]

# 전류는 가장 바깥쪽 격자에서 침투가 가능하다고 했으니 (x, y)에서 x는 0으로 고정되고 y만 움직이면서 dfs 호출
# (0,0)은 반복문으로 호출할 수 없어서 먼저 호출
dfs(graph, visited, 0, 0)
# (0,0)부터 (0,n)까지 호출
for i in range(n):
    dfs(graph, visited, 0, i + 1)

# 방문처리를 위한 리스트의 마지막 행에 1이 존재한다면 전류가 끝까지 침투한 것이니 YES
if 1 in visited[m - 1]:
    print('YES')
else:
    print('NO')

"""
맞긴 맞았는데 재귀 깊이가 백준 서버 상에서 설정해 놓은 값(1000)보다 깊어서 런타임 에러가 발생함.
그래서 sys.setrecursionlimit(10**6)를 통해 최대 재귀 깊이를 조정해서 정답은 맞췄다.
하지만 메모리 사용량이 너무 많다. 맞았는데 찝찝한 이 느낌
------------------------------------------------------------------------
bfs 사용해서 구현하니까 수행 시간에는 차이가 거의 없고 메모리 사용량이 10배 이상 개선됐다.
이 문제는 재귀 없이 반복문으로 푸는게 더 효율적인 풀이가 가능한 것 같다.
"""

# bfs 탐색
from collections import deque

def bfs(graph, visited):
    q = deque()
    # 맨 위줄 중 전류가 통하는 좌표만 큐에 추가
    for j in range(n):
        if graph[0][j] == 0:
            q.append((0, j))
    # 이동 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    check = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0 or visited[nx][ny] == 1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                # 좌표가 마지막 행까지 도달했을 경우
                if nx == m - 1:
                    check = True
                q.append((nx, ny))
                visited[nx][ny] = 1
                graph[nx][ny] = 1

    return check

m, n = map(int, input().split())
graph = []
# 격자 입력 받기
for _ in range(m):
    graph.append(list(map(int, input())))
# 방문처리를 위한 리스트
visited = [[0] * n for _ in range(m)]

if bfs(graph, visited):
    print('YES')
else:
    print('NO')
