import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

def dfs(now):
    # 방문 처리
    visited[now] = True
    # 현재 노드가 가리키고 있는 노드
    next_node = array[now]
    # i와 πi가 같으면 한 싸이클을 의미하므로 True 반환
    if next_node == now:
        return True

    # 방문하지 않은 연결된 노드를 dfs 탐색
    # 탐색이 모두 끝난 뒤 True 반환
    if not visited[next_node]:
        dfs(next_node)
        return True

t = int(input())

for _ in range(t):
    n = int(input())
    array = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    count = 0
    for i in range(1, n+1):
        if dfs(i):
            count += 1

    print(count)
