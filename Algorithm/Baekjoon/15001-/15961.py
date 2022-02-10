# 1, 시간 초과
import sys
from collections import deque
import itertools
input = sys.stdin.readline

n, nums, k, c = map(int, input().split())

array = deque()
for _ in range(n):
    array.append(int(input()))

answer = k
for i in range(len(array)):
    flag = False
    array.rotate(1)
    slice_arr = deque(itertools.islice(array, 0, k))

    for j in range(k):
        if slice_arr.count(array[j]) != 1:
            flag = True

    if flag:
        continue
    else:
        if c in slice_arr:
            continue
        else:
            if array[k] == c or array[-1] == c:
                answer += 1
                break

print(answer)

# 2, Sol
import sys
from collections import defaultdict
input = sys.stdin.readline

n, nums, k, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.extend(array) # 원형이므로 두개의 리스트 이어주기
table = defaultdict(int)

table[c] += 1 # 쿠폰은 항상 먹기

left = right = answer = 0
# k구간만큼 먹기
while right < k:
    table[array[right]] += 1
    right += 1

# 슬라이딩 윈도우 적용
while right < len(array):
    answer = max(answer, len(table))
    # 맨 왼쪽 초밥 제거
    table[array[left]] -= 1
    # 삭제 후 남은 초밥이 0 이면 제거
    if table[array[left]] == 0:
        del table[array[left]]
    # 오른쪽 초밥 추가
    table[array[right]] += 1
    # 슬라이딩 윈도우 확장
    left += 1
    right += 1

print(answer)