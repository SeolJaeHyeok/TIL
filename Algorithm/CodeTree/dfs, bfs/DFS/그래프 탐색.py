"""
N개의 정점과 M개의 간선으로 이루어진 양방향 그래프가 주어졌을 때,
1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수를 구하는 프로그램을 작성해보세요.
(여기서 1번 정점 자기 자신에 도달하는 경우는 가지수에서 제외합니다.)

Input
5 4         5 4
1 2         1 2
1 3         4 2
2 3         5 3
4 5         3 4

Output
2           4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[] * (m + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

count = 0


def dfs(v):
    global count
    visited[v] = True
    for cur_v in board[v]:
        if not visited[cur_v]:
            count += 1
            visited[cur_v] = True
            dfs(cur_v)


dfs(1)
print(count)