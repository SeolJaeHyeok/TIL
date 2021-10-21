# 음료수 얼려먹기
def dfs(x, y):
    # 범위를 벗어나면 False 리턴 후 함수 종료
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    # 해당 위치가 0이라면(구멍이 뚫려있는 부분이라면 == 아직 방문하지 않은 노드라면)
    if graph[x][y] == 0:
        graph[x][y] = 1  # 아이스크림으로 채우고 = 방문 처리하고
        # 동서남북 재귀적으로 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

count = 0
# 모든 위치(노드)를 시작점으로 해서 탐색
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
