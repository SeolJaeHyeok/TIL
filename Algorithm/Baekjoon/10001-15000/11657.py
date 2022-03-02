import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
graph = []
for _ in range(m):
    s, e, c = map(int, input().split())
    graph.append((s, e, c))

# 각 노드까지의 비용을 저장
answer = [INF] * (n + 1)
def process(start):
    answer[start] = 0 # 시작 노드 거리 0으로 초기화
    for i in range(n): # 노드 수만큼 반복
        for j in range(m): # 매 반복마다 모든 간선 확인
            currentNode = graph[j][0] # 현재 노드
            nextNode = graph[j][1] # 다음 노드
            cost = graph[j][2] # 거리 비용
            # 현재의 노드을 거쳐서 다른 노드로 이동하는 것이 더 짧을 경우 거리 갱신
            if answer[currentNode] != INF and answer[nextNode] > cost + answer[currentNode]:
                answer[nextNode] = cost + answer[currentNode]
                # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                if i == n - 1:
                    return False

    return True

if process(1):
    for i in range(2, len(answer)):
        if answer[i] == INF:
            print(-1)
        else:
            print(answer[i])
else:
    print(-1)

