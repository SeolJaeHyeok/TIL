import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, s, d = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
print(graph)

answer = 0
def dfs(cur_node, pre_node):
    global answer
    max_d = 0

    for next_node in graph[cur_node]:
        if next_node != pre_node:
            max_d = max(max_d, dfs(next_node, cur_node))

    if max_d >= d:
        print(cur_node, next_node)
        answer += 1

    return max_d + 1

dfs(s, 0)

print(2 * (answer - 1) if answer else 0)