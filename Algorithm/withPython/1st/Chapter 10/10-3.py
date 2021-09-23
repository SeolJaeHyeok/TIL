# 팀 결성
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

# 팀의 수와 연산의 수를 공백으로 구분하여 입력 받음
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)

# 모든 원소가 자기 자신을 부모로 가지도록 설정
for i in range(1, n + 1):
    parent[i] = i

# 모든 입력에 대하여 연산 수행
for i in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:  # 입력이 0이면 합치기 연산
        union_parent(parent, a, b)
    elif operation == 1:  # 입력이 1이면 찾기 연산
        if find_parent(parent, a) == find_parent(parent, b):  # 같은 부모 노드일 경우
            print('Yes')
        else:  # 서로 다른 부모 노드일 경
            print('No')

"""
전형적인 서로소 집합 알고리즘 문제
N과 M의 범위가 모두 100,000 이상이므로 경로 압축 기법을 통해 시간 복잡도를 개선

- 서로소 집합 알고리즘은 합치기 연산(union)과 찾기 연산(find)로 이루어짐
- 처음에는 각각의 노드의 부모 노드를 자기 자신으로 초기화 하고
- 0일 경우 합치기 연산을 수행: 두 노드의 루트 노드를 찾아 비교한 후 값이 더 큰 루트 노드가 작은 루트 노드를 부모 노드로 가리키도록 부모 테이블 갱신
- 1일 경우 찾기 연산을 수행: 입력된 두 노드의 루트 노드를 찾아 값을 비교한 후 같으면 Yes, 다르면 No 출력    
"""