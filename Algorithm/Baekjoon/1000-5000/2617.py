import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(v, graph):
    global count
    visited[v] = True

    for next_node in graph[v]:
        if not visited[next_node]:
            count += 1
            dfs(next_node, graph)

    # 해당 구슬보다 무거운 구슬이 절반 이상 => 중간이 될 가능성이 없는 구슬
    return count >= target

n, m = map(int, input().split())
target = (n + 1) // 2 # 총 구슬 개수의 절반
light = defaultdict(list) # 해당 구슬보다 가벼운 구슬을 담을 연결 리스트
heavy = defaultdict(list) # 해당 구슬보다 무거운 구슬을 담을 연결 리스트

array = []
for _ in range(m):
    array.append(list(map(int, input().split())))

for a, b in array:
    light[a].append(b)
    heavy[b].append(a)

answer = 0
# 모든 구슬을 검사해 해당 노드보다 가벼운 구슬 갯수 찾기
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    count = 0
    # 해당 구슬보다 가벼운 구슬이 절반 이상일 경우
    if dfs(i, light):
        answer += 1

# 모든 구슬을 검사해 해당 노드보다 무거운 구슬 갯수 찾기
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    count = 0
    # 해당 구슬보다 무거운 구슬이 절반 이상일 경우
    if dfs(i, heavy):
        answer += 1

print(answer)
