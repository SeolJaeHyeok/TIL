# 11866
# 1, deque의 rotate 함수 이용
from collections import deque

n, k = map(int, input().split())
array = deque()

for i in range(1, n + 1):
    array.append(i)

result = []
while array:
    # 왼쪽으로 2만큼 회전, 2만큼 해주는 이유는 K번째 요소를 제거하려면 K-1번째 요소까지 회전시켜야하기 때문이다.
    array.rotate(-(k - 1))
    result.append(array.popleft())

print('<', end='')
for i in range(len(result) - 1):
    print(f'{result[i]}, ', end='')
print(f'{result[-1]}>')


# 2, deque의 popleft이용

n, k = map(int, input().split())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

result = []
while queue:
    # 큐를 회전시키는 반복문 == deque의 rotate 함수와 동일
    for i in range(k-1):
        # k - 1번째까지 큐에서 빼낸 후 다시 마지막으로 추가
        queue.append(queue.popleft())
    # 회전 후 k번째 원소를 큐에서 제거
    result.append(queue.popleft())

print('<', end='')
for i in range(len(result) - 1):
    print(f'{result[i]}, ', end='')
print(f'{result[-1]}>')

"""
- 이 문제는 K-1번째 사람까지 큐에서 제거를 한 후에 큐에 맨 뒤로 다시 추가해주고 K번째 사람을 큐에서 완전히 제거해주면 된다.
- deque의 rotate 함수를 이용하여 큐를 회전시키는 방법과 popleft 함수를 이용하여 회전시키는 두 가지 방법이 있을 수 있다.
- rotate 함수는 요소를 제거하지 않고 리스트의 요소들을 회전시켜주는 함수다.
ex) 
[1, 2, 3, 4, 5]라는 큐가 있을 때
queue.rotate(3)을 하게 되면 오른쪽으로 3번 이동하게 된다. 따라서 [3, 4, 5, 1, 2]로 변한다.
queue.rotate(-3)을 하면 왼쪽으로 회전시킨다. 따라서 [4, 5, 1, 2, 3]으로 변한다.
"""