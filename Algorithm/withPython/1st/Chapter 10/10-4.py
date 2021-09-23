# 도시 분할 계획
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0  # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

"""
접근방법
전체 그래프에서 두 개의 최소 신장 트리를 만들어서 구현
최소한의 비용으로 2개의 신장 트리로 분할하기 위해 크루스칼 알고리즘으로 최소 신장 트리를 찾은 뒤에
최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거하는 것

- 크루스칼 알고리즘은 사이클을 발생시키는 간선은 제외하고 작은 비용부터 차례대로 집합에 추가하는 것
- 간선이 오름차순으로 정리되었기 때문에 사이클이 발생하지 않는 경우에 가장 마지막에 추간된 간선이 비용이 가장 높은 간선이다.
- 따라서 해당 간선을 결과에서 뺴준 뒤에 최종 결과를 출력  
"""
