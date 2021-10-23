# 회전하는 큐
# 데크 자료형과 rotate 메서드 이용
from collections import deque
n, m = map(int, input().split())
elements = list(map(int, input().split()))

# 데크 자료형으로 원소의 개수만큼 초기화(1 ~ n)
q = deque(i for i in range(1, n + 1))
count = 0

# 뽑아내려는 모든 위치 순회
for element in elements:
    # 뽑아내려는 원소의 위치가 첫 번째라면 뽑아내고 스킵
    if q.index(element) == 0:
        q.popleft()
        continue
    # 뽑아내려는 원소의 위치가 원소 배열의 길이 중간 이하 인덱스에 위치한다면
    elif q.index(element) <= len(q) // 2:
        # 해당 원소가 처음에 위치할 때까지 왼쪽으로 rotate
        while q.index(element) != 0:
            q.rotate(-1)
            count += 1
        # 그런 다음 추출
        q.popleft()
    # 뽑아내려는 원소의 위치가 원소 배열 길이의 중간보다 큰 인덱스에 위치한다면
    elif q.index(element) > len(q) // 2:
        # 해당 원소가 처음에 위치할 때까지 오른쪽으로 rotate
        while q.index(element) != 0:
            q.rotate(1)
            count += 1
        # 그런 다음 추출
        q.popleft()

print(count)
