# 1, 완전 탐색, 시간 초과
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(m)]
maxNum = max(nums)

answer = 1e9
for i in range(maxNum, 0, - 1):
    count = 0
    for num in nums:
        count += math.ceil(num / i)

    if count <= n:
        answer = min(answer, i)

print(answer)

# 2, 이분 탐색
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(m)]

start, end = 1, max(nums)
answer = 1e9
while start <= end:
    mid = (start + end) // 2 # 질투심

    # mid의 질투심을 가지고 나눠줄 수 있는 학생 수 구하기
    students = 0
    for num in nums:
        students += math.ceil(num / mid)

    # 구한 학생 수가 n보다 크다면 시작 값을 바꿔 질투심 증가시키기
    if students > n:
        start = mid + 1
    else: # n보다 작거나 같다면 정답 체크 먼저 하고, 질투심 감소시키기
        answer = min(answer, mid)
        end = mid - 1

print(answer)