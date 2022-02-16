# 1
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
array = [i for i in range(1, n + 1)]

# 1번째 풍선 처리
idx = 0
answer = []

now = nums.pop(idx) # 풍선에서 나온 현재 숫자값
answer.append(array.pop(idx)) # 터진 풍선 정답에 추가

while array:
    # 풍선 안에서 나온 값에 따라 다르게 처리
    if now > 0: # 양수일 경우
        # 오른쪽으로 이동
        idx = (idx + now - 1) % len(nums)
    else: # 음수일 경우
        # 왼쪽으로 이동
        idx = (idx + now) % len(nums)

    # 풍선에서 나온 값 갱신
    now = nums.pop(idx)
    # 터진 풍선 추가
    answer.append(array.pop(idx))

for i in answer:
    print(i, end=' ')

# 2, deque의 rotate 함수 이용
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))

answer = []
while q:
    idx, now = q.popleft()
    answer.append(idx + 1)
    if now > 0:
        q.rotate(-(now-1))
    else:
        q.rotate(-now)

for i in answer:
    print(i, end=' ')
