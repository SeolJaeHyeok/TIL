import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = 0
left, right = 0, len(arr) - 1

while left <= right:
    tmp = (right - left - 1) * min(arr[left], arr[right]) # left와 right를 양 끝으로 했을 경우 능력치
    answer = max(answer, tmp) # 능력치 최대값 갱신

    # 구간이 좁아질 수록 사이에 있는 개발자 수는 감소하지만 능력치의 최소값은 증가할 수 있다
    # 따라서 구간을 좁혀가면서 팀 능력치의 최대값을 찾아내야 한다
    # 그렇기 때문에 구간을 좁힐 때 left, right 포인터가 가리키는 값을 비교해 더 작은 포인터를 이동시킨다.
    if arr[left] < arr[right]:
        # left 포인터가 가리키는 값이 작으면 left 포인터 이동
        left += 1
    else:
        # right 포인터가 가리키는 값이 작으면 left 포인터 이동
        right -= 1

print(answer)

