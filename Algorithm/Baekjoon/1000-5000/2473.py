import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

flag = 10000000000 # 비교를 위한 임의의 비교 값
answer = [] # 세 용액을 담을 정답 리스트

# i를 기준으로 두고 i 이후의 값들을 이분 탐색
for i in range(n - 2):
    st = array[i] # 기준값
    left, right = i + 1, n - 1 # 기준값 이후의 시작값과 끝값

    while left < right:
        s = st + array[left] + array[right] # 세 용액의 합계
        # 세 용액의 합계를 비교 값과 비교
        # 작은 경우 정답과 비교 값 갱신
        if abs(s) <= abs(flag):
            answer = [st, array[left], array[right]]
            flag = s

        if s < 0: # 합이 0보다 작으면 왼쪽 값 증가
            left += 1
        elif s > 0: # 합이 0보다 크면 오른쪽 값 증가
            right -= 1
        else: # 합이 0이면 출력하고 종료
            print(*answer)
            sys.exit()

# 정답 출력
print(*answer)