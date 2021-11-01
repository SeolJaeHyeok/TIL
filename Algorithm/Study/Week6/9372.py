# 상근이의 여행
# DFS
import sys
t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    array = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())
        array[start].append(end)
        array[end].append(start)

    visited = [0] * (n + 1)
    count = 0
    def dfs(idx):
        global count
        visited[idx] = 1
        for i in array[idx]:
            if not visited[i]:
                dfs(i)
                count += 1

    dfs(1)
    print(count)

# 2, 모든 비행기가 연결되어있으므로 n-1을 하면 국가들 사이를 이동할 수 있는 최소 횟수
t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(m):
        start, end = map(int, sys.stdin.readline().split())

    print(n-1)