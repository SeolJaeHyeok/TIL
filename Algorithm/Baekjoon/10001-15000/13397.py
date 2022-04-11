import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

#
def f(mid):
    # 각 구간의 최대값과 최소값
    _max = _min = nums[0]
    count = 1
    # 배열을 순회하면서
    for i in range(1, len(nums)):
        # 최대값과 최소값을 지정하고
        _max = max(_max, nums[i])
        _min = min(_min, nums[i])

        # 그 차이가 기준값보다 크다면 기준값 포함 이전까지의 하나의 구간이 생긴 것
        # 따라서 최대값과 최소값을 갱신
        if _max - _min > mid:
            _max = nums[i]
            _min = nums[i]
            count += 1

    return count

# 시작값과 끝값 정의
start, end = 0, max(nums)
answer = 0
# 이분 탐색
while start <= end:
    # 비교를 할 기준값 정의
    mid = (start + end) // 2

    # 구간의 수가 m개 이하면 끝값을 줄이고 답 체크
    if f(mid) <= m:
        end = mid - 1
        answer = mid
    else: # m개 이상이면 시작 값 늘리기
        start = mid + 1

print(answer)